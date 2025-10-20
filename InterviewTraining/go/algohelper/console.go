package algohelper

import (
	"fmt"
	"os"
	"strings"
	"golang.org/x/term"
)

// Minimal console helpers to mimic JS coloring utilities.
// Provide ANSI coloring when stdout is a terminal.
var colorMap = map[string]string{
	"HEADER":  "35",
	"OKGREEN": "32",
	"FAIL":    "31",
	"WARNING": "33",
	"BOLD":    "1",
	"OKCYAN":  "36",
}

func isTerminal() bool {
	return term.IsTerminal(int(os.Stdout.Fd()))
}

func colorize(line string, code string) string {
	if !isTerminal() {
		return line
	}
	// allow multiple codes separated by comma
	parts := strings.Split(code, ",")
	return fmt.Sprintf("\x1b[%sm%s\x1b[0m", strings.Join(parts, ";"), line)
}

// PrintColor prints a line (colored when appropriate).
func PrintColor(line string) {
	fmt.Println(line)
}

// PrintColorWith prints a colored line using a color keyword from the map.
func PrintColorWith(line, color string) {
	if code, ok := colorMap[color]; ok {
		fmt.Println(colorize(line, code))
	} else {
		fmt.Println(line)
	}
}

// GetColorStr returns the possibly-colored string; default color when omitted.
func GetColorStr(line string, color ...string) string {
	if len(color) == 0 {
		if code, ok := colorMap["OKCYAN"]; ok {
			return colorize(line, code)
		}
		return line
	}
	if code, ok := colorMap[color[0]]; ok {
		return colorize(line, code)
	}
	return line
}
