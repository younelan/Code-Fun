//go:build problem

package main

func Solution(s string, key int) string {
	if key == 0 {
		return s
	}
	k := key % 26
	b := []byte(s)
	for i := range b {
		b[i] = byte(((int(b[i]-'a') + k) % 26) + 'a')
	}
	return string(b)
}
