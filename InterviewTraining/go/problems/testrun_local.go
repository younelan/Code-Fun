package main

import (
	"encoding/json"
	"fmt"
	"interviewtraining/algohelper"
	"os"
	"reflect"
	"strings"
)

// This local testrun is intended to be compiled together with a single problem
// file in the same directory. Usage: `go run problems/testrun_local.go problems/3sum.go 3sum`

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: go run problems/testrun_local.go <problemfile.go> -- <moduleName>\nOr: go run problems/testrun_local.go <problemfile.go> <moduleName>")
		os.Exit(1)
	}

	// Allow passing module name after `--` (like: go run ... testrun_local.go 3sum.go -- 3sum)
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
		fmt.Println("Missing module name. See usage.")
		os.Exit(1)
	}

	tests, err := algohelper.LoadTests(moduleName)
	if err != nil {
		fmt.Printf("Error loading tests for %s: %v\n", moduleName, err)
		os.Exit(1)
	}
	if len(tests) == 0 {
		fmt.Printf("No tests found for module '%s'\n", moduleName)
		return
	}

	algohelper.PrintColorWith(fmt.Sprintf("---- Test %s ----", moduleName), "HEADER")
	passed := 0
	failed := 0

	for idx, test := range tests {
		prefix := fmt.Sprintf("Test %d:", idx+1)
		testType, _ := test["testType"].(string)

		// Backwards-compat: some JSON test files omit testType and provide
		// fields like `array`/`target` or `input`. Normalize to a function test.
		if testType == "" {
			if _, ok := test["input"]; ok {
				testType = "function"
			} else if _, aok := test["array"]; aok {
				// e.g. binsearch.json: has `array` and `target` fields
				testType = "function"
				test["input"] = []interface{}{test["array"], test["target"]}
			}
		}

		var result interface{}
		var runErr error

		// Normalize legacy shapes; keep function-style mostly unchanged.
		switch testType {
		case "function":
			input := test["input"]
			// Per-file contract: problems provide a `Solution` function.
			rv := reflect.ValueOf(Solution)
			if rv.Kind() != reflect.Func {
				fmt.Println("  No Solution function found; skipping execution")
			} else {
				args := toReflectArgs(input, rv.Type())
				out := rv.Call(args)
				if len(out) > 0 {
					result = out[0].Interface()
				}
			}
		case "list":
			nodesRaw, _ := test["nodes"].([]interface{})
			nodes := toMapSlice(nodesRaw)
			headId, _ := test["headId"].(string)
			head, _ := algohelper.LoadList(nodes, headId)
			rv := reflect.ValueOf(Solution)
			if rv.Kind() != reflect.Func {
				fmt.Println("  No Solution function found; skipping list test")
			} else {
				out := rv.Call([]reflect.Value{reflect.ValueOf(head)})
				if len(out) > 0 {
					result = out[0].Interface()
				}
			}
		case "graph":
			graphRaw := test["graph"].(map[string]interface{})
			nodesRaw, _ := graphRaw["nodes"].([]interface{})
			nodes := toMapSlice(nodesRaw)
			startNodeId, _ := graphRaw["startNode"].(string)
			className, _ := test["className"].(string)
			methodName, _ := test["method"].(string)

			// Use centralized algohelper helpers to instantiate and wire nodes.
			ctor := New
			insts, _ := algohelper.InstantiateGraph(nodes, ctor)
			algohelper.AttachChildren(insts, nodes)
			start := insts[startNodeId]
			m := start.MethodByName(upperFirst(methodName))
			if !m.IsValid() {
				fmt.Printf("  Method %s not found on class %s\n", methodName, className)
			} else {
				out := m.Call([]reflect.Value{reflect.ValueOf([]interface{}{})})
				if len(out) > 0 {
					result = out[0].Interface()
				}
			}

		case "tree":
			// tree tests describe a tree structure under `tree` key
			treeRaw, _ := test["tree"].(map[string]interface{})
			nodesRaw, _ := treeRaw["nodes"].([]interface{})
			nodes := toMapSlice(nodesRaw)
			// root id can be 'root' or 'rootId'
			rootId := ""
			if v, ok := treeRaw["root"].(string); ok {
				rootId = v
			}
			if v, ok := treeRaw["rootId"].(string); ok {
				rootId = v
			}
			root, _ := algohelper.BuildTree(nodes, rootId)
			rv := reflect.ValueOf(Solution)
			if rv.Kind() != reflect.Func {
				fmt.Println("  No Solution function found; skipping tree test")
			} else {
				out := rv.Call([]reflect.Value{reflect.ValueOf(root)})
				if len(out) > 0 {
					result = out[0].Interface()
				}
			}
		default:
			fmt.Printf("  Unrecognized testType: %s\n", testType)
		}

		expected := test["expect"]
		if expected == nil {
			expected = test["expected"]
		}

		passedTest := equals(result, expected)
		if passedTest {
			passed++
			fmt.Printf("%s %s\n", prefix, algohelper.GetColorStr("Passed", "OKGREEN"))
		} else {
			failed++
			fmt.Printf("%s %s\n", prefix, algohelper.GetColorStr("Failed", "FAIL"))
			fmt.Printf("  Returned: %s\n", algohelper.GetColorStr(formatValue(result), "FAIL"))
			fmt.Printf("  Expected: %s\n\n", algohelper.GetColorStr(formatValue(expected), "OKGREEN"))
		}
		if runErr != nil {
			fmt.Printf("  Error: %v\n", runErr)
		}
	}

	total := passed + failed
	fmt.Printf("Total Tests: %d\nPassed: %d\nFailed: %d\n", total, passed, failed)
}

func toMapSlice(raw []interface{}) []map[string]interface{} {
	out := make([]map[string]interface{}, 0, len(raw))
	for _, v := range raw {
		if m, ok := v.(map[string]interface{}); ok {
			out = append(out, m)
		}
	}
	return out
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
	// return zero value to avoid reflect.Call panics for incompatible types
	return reflect.Zero(t)
}

func equals(a interface{}, b interface{}) bool {
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

func upperFirst(s string) string {
	if s == "" {
		return s
	}
	return strings.ToUpper(s[:1]) + s[1:]
}
