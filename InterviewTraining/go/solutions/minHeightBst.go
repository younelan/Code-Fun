//go:build problem

package main

// Local BST type (self-contained so this file compiles when run alone).
type BST struct {
    Value int
    Left  *BST
    Right *BST
}

// Solution builds a minimum-height BST from a sorted array provided as input.
// Accepts either a []int directly or the normalized input from the runner.
func Solution(input interface{}) *BST {
    var arr []int
    if a, ok := input.([]int); ok {
        arr = a
    } else if aa, ok := input.([]interface{}); ok {
        for _, v := range aa {
            if f, ok := v.(float64); ok {
                arr = append(arr, int(f))
            }
        }
    }
    if len(arr) == 0 {
        return nil
    }
    // ensure sorted - tests provide sorted input but be defensive
    // build recursively
    var build func(l, r int) *BST
    build = func(l, r int) *BST {
        if l > r {
            return nil
        }
        mid := (l + r) / 2
        node := &BST{Value: arr[mid]}
        node.Left = build(l, mid-1)
        node.Right = build(mid+1, r)
        return node
    }
    return build(0, len(arr)-1)
}
