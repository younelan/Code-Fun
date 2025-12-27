//go:build problem

package main

func Solution(arr []int) int {
	seen := map[int]int{}
	for _, v := range arr {
		seen[v]++
		if seen[v] > 1 {
			return v
		}
	}
	return -1
}
