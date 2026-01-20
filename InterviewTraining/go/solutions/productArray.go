//go:build problem

package main

// Product array except self
func Solution(nums []int) []int {
	n := len(nums)
	left := make([]int, n)
	right := make([]int, n)
	res := make([]int, n)
	prod := 1
	for i := 0; i < n; i++ {
		left[i] = prod
		prod *= nums[i]
	}
	prod = 1
	for i := n - 1; i >= 0; i-- {
		right[i] = prod
		prod *= nums[i]
	}
	for i := 0; i < n; i++ {
		res[i] = left[i] * right[i]
	}
	return res
}
