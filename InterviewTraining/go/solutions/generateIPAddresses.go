//go:build problem

package main

import "strconv"

func validPart(s string) bool {
	if len(s) == 0 || len(s) > 3 {
		return false
	}
	if len(s) > 1 && s[0] == '0' {
		return false
	}
	v, err := strconv.Atoi(s)
	if err != nil {
		return false
	}
	return v >= 0 && v <= 255
}

func Solution(s string) []string {
	n := len(s)
	res := []string{}
	for i := 1; i <= 3 && i < n-2; i++ {
		for j := i + 1; j <= i+3 && j < n-1; j++ {
			for k := j + 1; k <= j+3 && k < n; k++ {
				a := s[:i]
				b := s[i:j]
				c := s[j:k]
				d := s[k:]
				if validPart(a) && validPart(b) && validPart(c) && validPart(d) {
					res = append(res, a+"."+b+"."+c+"."+d)
				}
			}
		}
	}
	return res
}
