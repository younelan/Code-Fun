//go:build problem

package main

import "sort"

// classPhotos: determine if two arrays can be arranged into two rows
// so that every student in one row is strictly taller than the corresponding student in the other row.
func Solution(redHeights []int, blueHeights []int) bool {
    if len(redHeights) != len(blueHeights) {
        return false
    }
    sort.Ints(redHeights)
    sort.Ints(blueHeights)
    // Tests expect the first argument to be the front row (shorter).
    for i := 0; i < len(redHeights); i++ {
        if !(redHeights[i] < blueHeights[i]) {
            return false
        }
    }
    return true
}
