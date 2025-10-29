//go:build problem

package main

func Solution(characters string, note string) bool {
	freq := map[rune]int{}
	for _, ch := range characters {
		freq[ch]++
	}
	for _, ch := range note {
		if freq[ch] == 0 {
			return false
		}
		freq[ch]--
	}
	return true
}
