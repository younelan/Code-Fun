//go:build problem

package main

import "fmt"

// Solution accepts `nodes` (array of node objects) and `headId` and returns the
// list of values after removing duplicates (matching test expectation shape).
func Solution(nodes []interface{}, headId string) []int {
    // build map of id -> node struct
    type node struct {
        val  int
        next *string
    }
    m := map[string]*node{}
    for _, ni := range nodes {
        n := ni.(map[string]interface{})
        id := fmt.Sprintf("%v", n["id"])
        v := 0
        if vv, ok := n["value"].(float64); ok {
            v = int(vv)
        }
        var next *string
        if n["next"] != nil {
            s := fmt.Sprintf("%v", n["next"])
            next = &s
        }
        m[id] = &node{val: v, next: next}
    }
    // traverse starting at headId, collect values
    order := []int{}
    curId := headId
    visited := map[string]bool{}
    for curId != "" && !visited[curId] {
        visited[curId] = true
        n := m[curId]
        order = append(order, n.val)
        if n.next == nil {
            break
        }
        curId = *n.next
    }
    // remove duplicates from order (assumes order is sorted? tests expect removing
    // consecutive duplicates in original list). We'll remove consecutive duplicates.
    if len(order) == 0 {
        return order
    }
    res := []int{order[0]}
    for i := 1; i < len(order); i++ {
        if order[i] != res[len(res)-1] {
            res = append(res, order[i])
        }
    }
    return res
}
