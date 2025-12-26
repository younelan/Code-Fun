//go:build problem

package main

import "sort"

func Solution(nums []int) []int {
	if len(nums) < 3 {
		return nums
	}
	sort.Ints(nums)
	n := len(nums)
	return []int{nums[n-3], nums[n-2], nums[n-1]}
}
