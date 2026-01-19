//go:build problem

package main

func Solution(array []int) []int {
	set := map[int]bool{}
	for _, v := range array {
		set[v] = true
	}

bestLen := 0
bestStart := 0

for v := range set {
	// if there's a lower neighbor, skip (we'll handle at the lowest start)
 	if set[v-1] {
 		continue
 	}

	current := v
	length := 1
	for set[current+1] {
		current++
		length++
	}
	if length > bestLen {
		bestLen = length
		bestStart = v
	}
}

return []int{bestStart, bestStart + bestLen - 1}
}
