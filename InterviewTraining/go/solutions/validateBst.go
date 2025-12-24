//go:build problem

package main

import "fmt"

// Solution accepts a tree JSON object and returns whether it's a valid BST.
func Solution(treeObj map[string]interface{}) bool {
    nodesVal, ok := treeObj["nodes"].([]interface{})
    if !ok {
        return false
    }
    m := map[string]map[string]interface{}{}
    var rootId string
    for _, ni := range nodesVal {
        n := ni.(map[string]interface{})
        id := fmt.Sprintf("%v", n["id"])
        m[id] = n
        if rootId == "" {
            rootId = id
        }
    }
    if r, ok := treeObj["rootId"].(string); ok {
        rootId = r
    }
    if r, ok := treeObj["root"].(string); ok {
        rootId = r
    }

    var dfs func(id string, min, max *float64) bool
    dfs = func(id string, min, max *float64) bool {
        if id == "" {
            return true
        }
        n, ok := m[id]
        if !ok {
            return true
        }
        val := n["value"].(float64)
        if min != nil && val <= *min {
            return false
        }
        if max != nil && val >= *max {
            return false
        }
        var leftId, rightId string
        if l, ok := n["left"].(string); ok {
            leftId = l
        }
        if r, ok := n["right"].(string); ok {
            rightId = r
        }
        // left subtree must be < val
        if !dfs(leftId, min, &val) {
            return false
        }
        // right subtree must be > val
        if !dfs(rightId, &val, max) {
            return false
        }
        return true
    }
    return dfs(rootId, nil, nil)
}
