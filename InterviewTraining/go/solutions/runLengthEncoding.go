//go:build problem

package main

import "strconv"

// run-length encoding
func Solution(s string) string {
	if s == "" {
		return ""
	}
	res := ""
	count := 1
	prev := s[0]
	for i := 1; i < len(s); i++ {
		if s[i] == prev {
			count++
		} else {
			// Split runs into chunks of max 9 as expected by tests
			for count > 9 {
				res += "9" + string(prev)
				count -= 9
			}
			res += strconv.Itoa(count) + string(prev)
			prev = s[i]
			count = 1
		}
	}
	for count > 9 {
		res += "9" + string(prev)
		count -= 9
	}
	res += strconv.Itoa(count) + string(prev)
	return res
}
