//go:build problem

package main

import (
    "strings"
)

func Solution(s string) string {
    // split by whitespace, collapsing multiple spaces
    parts := strings.Fields(s)
    for i, j := 0, len(parts)-1; i < j; i, j = i+1, j-1 {
        parts[i], parts[j] = parts[j], parts[i]
    }
    return strings.Join(parts, " ")
}
