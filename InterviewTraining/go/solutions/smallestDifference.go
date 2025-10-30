//go:build problem

package main

import "sort"

// smallestDifference: returns pair with smallest absolute difference
func Solution(a []int, b []int) []int {
	sort.Ints(a)
	sort.Ints(b)
	i, j := 0, 0
	best := 1<<63 - 1
	var pair []int
	for i < len(a) && j < len(b) {
		da := a[i] - b[j]
		if abs(da) < best {
			best = abs(da)
			pair = []int{a[i], b[j]}
		}
		if a[i] < b[j] {
			i++
		} else {
			j++
		}
	}
	return pair
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
