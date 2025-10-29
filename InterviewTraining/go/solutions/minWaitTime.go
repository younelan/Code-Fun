//go:build problem

package main

import "sort"

func Solution(queries []int) int {
	if len(queries) < 2 {
		return 0
	}
	sort.Ints(queries)
	total := 0
	current := 0
	for _, q := range queries {
		total += current
		current += q
	}
	return total
}
