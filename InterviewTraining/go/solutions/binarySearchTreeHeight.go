//go:build problem

package main

import "fmt"

// Solution accepts a `tree` JSON object and returns its height.
func Solution(treeObj map[string]interface{}) int {
    // treeObj: {"nodes": [...], "rootId" or "root"}
    nodesVal, ok := treeObj["nodes"].([]interface{})
    if !ok {
        return 0
    }
    // build maps
    left := map[string]*string{}
    right := map[string]*string{}
    var rootId string
    if r, ok := treeObj["rootId"].(string); ok {
        rootId = r
    }
    if r, ok := treeObj["root"].(string); ok && rootId == "" {
        rootId = r
    }
    for _, ni := range nodesVal {
        n := ni.(map[string]interface{})
        id := fmt.Sprintf("%v", n["id"])
        if leftId, ok := n["left"].(string); ok {
            l := leftId
            left[id] = &l
        } else {
            left[id] = nil
        }
        if rightId, ok := n["right"].(string); ok {
            r := rightId
            right[id] = &r
        } else {
            right[id] = nil
        }
        if rootId == "" {
            rootId = id
        }
    }

    var height func(id string) int
    height = func(id string) int {
        if id == "" {
            return 0
        }
        l := 0
        r := 0
        if left[id] != nil {
            l = height(*left[id])
        }
        if right[id] != nil {
            r = height(*right[id])
        }
        if l > r {
            return l + 1
        }
        return r + 1
    }
    if rootId == "" {
        return 0
    }
    return height(rootId)
}
