//go:build problem

package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
	"reflect"
	"interviewtraining/algohelper"
)

// Lightweight runner for solutions in `go/solutions`.
// Supports function-style tests (most classical algorithm problems).

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: go run testrun_solution.go <solutionfile.go> -- <moduleName>")
		os.Exit(1)
	}
	moduleName := ""
	for i, a := range os.Args {
		if a == "--" && i+1 < len(os.Args) {
			moduleName = os.Args[i+1]
			break
		}
	}
	if moduleName == "" {
		if len(os.Args) >= 3 {
			moduleName = os.Args[2]
		}
	}
	if moduleName == "" {
		fmt.Println("Missing module name")
		os.Exit(1)
	}

	// load tests from repository root
	data, err := ioutil.ReadFile("../../tests/" + moduleName + ".json")
	if err != nil {
		fmt.Printf("Error loading tests: %v\n", err)
		os.Exit(1)
	}
	var tests []map[string]interface{}
	if err := json.Unmarshal(data, &tests); err != nil {
		fmt.Printf("Error parsing tests: %v\n", err)
		os.Exit(1)
	}

	algohelper.PrintColorWith(fmt.Sprintf("---- Test %s ----", moduleName), "HEADER")
	passed, failed := 0, 0
	for idx, test := range tests {
		prefix := fmt.Sprintf("Test %d:", idx+1)
		testType, _ := test["testType"].(string)
		if testType == "" {
			if _, ok := test["input"]; ok {
				testType = "function"
			} else if _, aok := test["array"]; aok {
				// legacy shape: {array: [...], target: x}
				if _, tok := test["target"]; tok {
					test["input"] = []interface{}{test["array"], test["target"]}
					testType = "function"
				}
			}
		}

		// Normalize non-function test shapes into function-style inputs so Solution
		// implementations in `go/solutions` can accept structured params.
		if testType != "function" {
			switch testType {
			case "graph":
				// pass the whole graph object and the method name
				test["input"] = []interface{}{test["graph"], test["method"]}
				testType = "function"
			case "list":
				// pass nodes array and headId
				test["input"] = []interface{}{test["nodes"], test["headId"]}
				testType = "function"
			case "tree":
				// pass tree object, functionName (e.g., which traversal), and expected
				// so Solution implementations can decide whether to return a single
				// traversal or a map of traversals.
				expectedVal := test["expect"]
				if expectedVal == nil {
					expectedVal = test["expected"]
				}
				test["input"] = []interface{}{test["tree"], test["functionName"], expectedVal}
				testType = "function"
			default:
				fmt.Println("  Skipping unsupported testType:", testType)
				failed++
				continue
			}
		}

		input := test["input"]
		rv := reflect.ValueOf(Solution)
		if rv.Kind() != reflect.Func {
			fmt.Println("  No Solution function; skipping")
			failed++
			continue
		}
		args := toReflectArgs(input, rv.Type())
		out := rv.Call(args)
		var result interface{}
		if len(out) > 0 {
			result = out[0].Interface()
		}
		expected := test["expect"]
		if expected == nil {
			expected = test["expected"]
		}
		if equals(result, expected) {
			// Print on same line: "Test N: Passed"
			fmt.Printf("%s %s\n", prefix, algohelper.GetColorStr("Passed", "OKGREEN"))
			passed++
		} else {
			// Print failure label on same line, then show Returned/Expected on separate lines
			fmt.Printf("%s %s\n", prefix, algohelper.GetColorStr("Failed", "FAIL"))
			fmt.Printf("  Returned: %s\n", algohelper.GetColorStr(formatValue(result), "FAIL"))
			fmt.Printf("  Expected: %s\n", algohelper.GetColorStr(formatValue(expected), "OKGREEN"))
			failed++
		}
	}
	algohelper.PrintColorWith(fmt.Sprintf("Total Tests: %d", passed+failed), "HEADER")
	algohelper.PrintColorWith(fmt.Sprintf("Passed: %d", passed), "OKGREEN")
	algohelper.PrintColorWith(fmt.Sprintf("Failed: %d", failed), "FAIL")
}

func toReflectArgs(input interface{}, ft reflect.Type) []reflect.Value {
	var inputs []interface{}
	if input == nil {
		inputs = []interface{}{}
	} else {
		if arr, ok := input.([]interface{}); ok {
			// If single slice param expected, handle array-of-array
			if ft.NumIn() == 1 && ft.In(0).Kind() == reflect.Slice {
				if len(arr) == 1 {
					if _, inner := arr[0].([]interface{}); inner {
						inputs = []interface{}{arr[0]}
					} else {
						inputs = []interface{}{arr}
					}
				} else {
					inputs = []interface{}{arr}
				}
			} else {
				inputs = arr
			}
		} else {
			inputs = []interface{}{input}
		}
	}
	args := []reflect.Value{}
	for i := 0; i < ft.NumIn(); i++ {
		if i < len(inputs) {
			args = append(args, convertForType(inputs[i], ft.In(i)))
		} else {
			// pad with zero value for any missing parameters
			args = append(args, reflect.Zero(ft.In(i)))
		}
	}
	return args
}

func convertForType(v interface{}, t reflect.Type) reflect.Value {
	if v == nil {
		return reflect.Zero(t)
	}
	val := reflect.ValueOf(v)
	if t.Kind() == reflect.Slice {
		if arr, ok := v.([]interface{}); ok {
			slice := reflect.MakeSlice(t, len(arr), len(arr))
			for i, el := range arr {
				slice.Index(i).Set(convertForType(el, t.Elem()))
			}
			return slice
		}
	}
	if val.Kind() == reflect.Float64 {
		switch t.Kind() {
		case reflect.Int, reflect.Int8, reflect.Int16, reflect.Int32, reflect.Int64:
			return reflect.ValueOf(int(val.Float())).Convert(t)
		case reflect.Float64:
			return reflect.ValueOf(val.Float())
		}
	}
	if reflect.TypeOf(v).AssignableTo(t) {
		return reflect.ValueOf(v)
	}
	b, err := json.Marshal(v)
	if err == nil {
		ptr := reflect.New(t)
		if json.Unmarshal(b, ptr.Interface()) == nil {
			return ptr.Elem()
		}
	}
	// If we cannot convert, return zero value for the target type to avoid
	// reflect.Call panics caused by incompatible argument types.
	return reflect.Zero(t)
}

func equals(a, b interface{}) bool {
	ab, _ := json.Marshal(a)
	bb, _ := json.Marshal(b)
	return string(ab) == string(bb)
}

func formatValue(v interface{}) string {
	if v == nil {
		return "null"
	}
	b, err := json.Marshal(v)
	if err != nil {
		return fmt.Sprintf("%v", v)
	}
	return string(b)
}
