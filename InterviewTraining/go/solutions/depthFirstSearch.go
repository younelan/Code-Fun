//go:build problem

package main

// Depth-first search solution that accepts the graph JSON structure and a method name.
// The test runner normalizes graph tests to call `Solution(graphObj, methodName)`.

import "fmt"

func Solution(graphObj map[string]interface{}, method string) []string {
    // graphObj contains {"nodes": [...], "startNode"/"rootId":...}
    nodesVal, ok := graphObj["nodes"].([]interface{})
    if !ok {
        return []string{}
    }
    // build adjacency map and start id
    children := map[string][]string{}
    var start string
    if s, ok := graphObj["startNode"].(string); ok {
        start = s
    }
    if s, ok := graphObj["root"].(string); ok && start == "" {
        start = s
    }
    if s, ok := graphObj["rootId"].(string); ok && start == "" {
        start = s
    }
    for _, ni := range nodesVal {
        n := ni.(map[string]interface{})
        id := fmt.Sprintf("%v", n["id"])
        if start == "" {
            // pick the first id as start if none provided
            start = id
        }
        chs := []string{}
        if raw, ok := n["children"].([]interface{}); ok {
            for _, c := range raw {
                chs = append(chs, fmt.Sprintf("%v", c))
            }
        }
        children[id] = chs
    }

    // perform DFS
    res := []string{}
    var dfs func(id string)
    dfs = func(id string) {
        res = append(res, id)
        for _, c := range children[id] {
            dfs(c)
        }
    }
    if start != "" {
        dfs(start)
    }
    return res
}
