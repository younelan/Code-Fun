//go:build problem

package main

import "sort"

// minimum characters for words
func Solution(words []string) []string {
	freq := map[rune]int{}
	for _, w := range words {
		local := map[rune]int{}
		for _, ch := range w {
			local[ch]++
			if local[ch] > freq[ch] {
				freq[ch] = local[ch]
			}
		}
	}
	res := []string{}
	for ch, cnt := range freq {
		for i := 0; i < cnt; i++ {
			res = append(res, string(ch))
		}
	}
	sort.Strings(res)
	return res
}
