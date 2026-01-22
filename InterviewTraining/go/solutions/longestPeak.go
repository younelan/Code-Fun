//go:build problem

package main

func Solution(array []int) int {
    n := len(array)
    if n < 3 {
        return 0
    }

    maxLen := 0
    i := 1
    for i <= n-2 {
        // find a peak
        if array[i-1] < array[i] && array[i] > array[i+1] {
            left := i - 1
            for left-1 >= 0 && array[left-1] < array[left] {
                left--
            }
            right := i + 1
            for right+1 < n && array[right+1] < array[right] {
                right++
            }
            length := right - left + 1
            if length > maxLen {
                maxLen = length
            }
            i = right + 1
        } else {
            i++
        }
    }
    return maxLen
}
