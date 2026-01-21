//go:build problem

package main

// Solution accepts nodes JSON and headId and returns whether a cycle exists.
func Solution(nodes []map[string]interface{}, headId string) bool {
    // build next map
    next := map[string]*string{}
    for _, n := range nodes {
        id := n["id"].(string)
        if n["next"] == nil {
            next[id] = nil
        } else {
            s := n["next"].(string)
            next[id] = &s
        }
    }
    // tortoise and hare using ids
    if headId == "" {
        return false
    }
    slow := headId
    fast := headId
    for {
        // advance slow by 1
        if next[slow] == nil {
            return false
        }
        slow = *next[slow]
        // advance fast by 2
        if next[fast] == nil {
            return false
        }
        f1 := next[fast]
        if f1 == nil {
            return false
        }
        if next[*f1] == nil {
            return false
        }
        fast = *next[*f1]
        if slow == fast {
            return true
        }
    }
}
