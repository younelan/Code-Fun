//go:build problem

package main

func Solution(s string) int {
    counts := map[rune]int{}
    for _, r := range s {
        counts[r]++
    }
    idx := 0
    for _, r := range s {
        if counts[r] == 1 {
            return idx
        }
        idx++
    }
    return -1
}
