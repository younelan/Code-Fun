//go:build problem

package main

func Solution(arr []int) []int {
	n := len(arr)
	if n <= 1 {
		return []int{-1, -1}
	}
	left := 0
	for left < n-1 && arr[left] <= arr[left+1] {
		left++
	}
	if left == n-1 {
		return []int{-1, -1}
	}
	right := n - 1
	for right > 0 && arr[right] >= arr[right-1] {
		right--
	}
	subMin, subMax := arr[left], arr[left]
	for i := left; i <= right; i++ {
		if arr[i] < subMin {
			subMin = arr[i]
		}
		if arr[i] > subMax {
			subMax = arr[i]
		}
	}
	for i := 0; i < left; i++ {
		if arr[i] > subMin {
			left = i
			break
		}
	}
	for i := n - 1; i > right; i-- {
		if arr[i] < subMax {
			right = i
			break
		}
	}
	return []int{left, right}
}
