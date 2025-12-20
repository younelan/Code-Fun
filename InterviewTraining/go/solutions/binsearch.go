//go:build problem

package main

// Binary search: returns index of target or -1
func Solution(arr []int, target int) int {
	l, r := 0, len(arr)-1
	for l <= r {
		m := (l + r) / 2
		if arr[m] == target {
			return m
		} else if arr[m] < target {
			l = m + 1
		} else {
			r = m - 1
		}
	}
	return -1
}
