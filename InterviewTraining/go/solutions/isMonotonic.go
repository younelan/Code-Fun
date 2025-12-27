//go:build problem

package main

func Solution(arr []int) bool {
	if len(arr) <= 2 {
		return true
	}
	inc, dec := true, true
	for i := 1; i < len(arr); i++ {
		if arr[i] < arr[i-1] {
			inc = false
		}
		if arr[i] > arr[i-1] {
			dec = false
		}
	}
	return inc || dec
}
