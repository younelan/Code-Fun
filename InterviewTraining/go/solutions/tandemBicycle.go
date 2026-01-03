//go:build problem

package main

import "sort"

// tandem bicycle takes two arrays of speeds and a boolean fastestTeam
// if fastestTeam true, pair to maximize sum, else minimize
func Solution(redShirtSpeeds []int, blueShirtSpeeds []int, fastestTeam bool) int {
	sort.Ints(redShirtSpeeds)
	sort.Ints(blueShirtSpeeds)
	n := len(redShirtSpeeds)
	total := 0
	if fastestTeam {
		for i := 0; i < n; i++ {
			a := redShirtSpeeds[i]
			b := blueShirtSpeeds[n-1-i]
			if a > b {
				total += a
			} else {
				total += b
			}
		}
	} else {
		for i := 0; i < n; i++ {
			a := redShirtSpeeds[i]
			b := blueShirtSpeeds[i]
			if a > b {
				total += a
			} else {
				total += b
			}
		}
	}
	return total
}
