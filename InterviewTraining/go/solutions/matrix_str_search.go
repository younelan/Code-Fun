//go:build problem

package main

// returns [found bool, direction string]
func Solution(M [][]string, S string) []interface{} {
	dirs := []struct {
		dx, dy int
		name   string
	}{
		{-1, 0, "north"}, {1, 0, "south"}, {0, 1, "east"}, {0, -1, "west"}, {1, 1, "south-east"}, {1, -1, "south-west"},
	}
	rows := len(M)
	if rows == 0 {
		return []interface{}{false, ""}
	}
	cols := len(M[0])
	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			if M[i][j] != string(S[0]) {
				continue
			}
			for _, d := range dirs {
				x, y := i, j
				k := 0
				for k < len(S) {
					if x < 0 || x >= rows || y < 0 || y >= cols || M[x][y] != string(S[k]) {
						break
					}
					x += d.dx
					y += d.dy
					k++
				}
				if k == len(S) {
					return []interface{}{true, d.name}
				}
			}
		}
	}
	return []interface{}{false, ""}
}
