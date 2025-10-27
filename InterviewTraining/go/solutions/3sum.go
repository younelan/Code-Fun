//go:build problem

package main

import "sort"

// Solution for threeNumberSum: returns sorted triplets that sum to target.
// Ported from js/solutions/3sum.js: use triple nested loops over sorted array.
func Solution(nums []int, target int) [][]int {
    arr := make([]int, len(nums))
    copy(arr, nums)
    sort.Ints(arr)
    res := [][]int{}
    n := len(arr)
    for i := 0; i < n-2; i++ {
        for j := i + 1; j < n-1; j++ {
            for k := j + 1; k < n; k++ {
                if arr[i]+arr[j]+arr[k] == target {
                    res = append(res, []int{arr[i], arr[j], arr[k]})
                }
            }
        }
    }
    return res
}
