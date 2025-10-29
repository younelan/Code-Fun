//go:build problem

package main

import "sort"

// mergeOverlappingIntervals alias for mergeIntervals tests
func Solution(intervals [][]int) [][]int {
    if len(intervals) == 0 {
        return [][]int{}
    }
    sort.Slice(intervals, func(i, j int) bool {
        if intervals[i][0] == intervals[j][0] {
            return intervals[i][1] < intervals[j][1]
        }
        return intervals[i][0] < intervals[j][0]
    })
    res := [][]int{intervals[0]}
    for i := 1; i < len(intervals); i++ {
        last := res[len(res)-1]
        cur := intervals[i]
        if cur[0] <= last[1] {
            if cur[1] > last[1] {
                last[1] = cur[1]
            }
            res[len(res)-1] = last
        } else {
            res = append(res, []int{cur[0], cur[1]})
        }
    }
    return res
}
