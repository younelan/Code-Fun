//go:build problem

package main

func Solution(matrix [][]int) []int {
	if len(matrix) == 0 || len(matrix[0]) == 0 {
		return []int{}
	}
	top, left := 0, 0
	bottom, right := len(matrix)-1, len(matrix[0])-1
	res := []int{}
	for top <= bottom && left <= right {
		for j := left; j <= right; j++ {
			res = append(res, matrix[top][j])
		}
		for i := top + 1; i <= bottom; i++ {
			res = append(res, matrix[i][right])
		}
		if top < bottom {
			for j := right - 1; j >= left; j-- {
				res = append(res, matrix[bottom][j])
			}
		}
		if left < right {
			for i := bottom - 1; i > top; i-- {
				res = append(res, matrix[i][left])
			}
		}
		top++
		bottom--
		left++
		right--
	}
	return res
}
