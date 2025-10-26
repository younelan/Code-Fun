//go:build ignore

package main

import (
	"encoding/json"
	"fmt"
	"interviewtraining/algohelper"
	"os"
	"reflect"
	"strings"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: go run testrun.go <moduleName>")
		os.Exit(1)
	}
	moduleName := os.Args[1]

	// Call the module's Exports() function which must be provided by the
	// problem file compiled alongside this runner (we run: go run testrun.go problems/<mod>.go).
	exports := Exports()

	tests, err := algohelper.LoadTests(moduleName)
	if err != nil {
		fmt.Printf("Error loading tests for %s: %v\n", moduleName, err)
		os.Exit(1)
	}
	if len(tests) == 0 {
		fmt.Printf("No tests found for module '%s'\n", moduleName)
		return
	}

	fmt.Printf("---- Test %s ----\n", moduleName)
	passed := 0
	failed := 0

	for idx, test := range tests {
		fmt.Printf("Test %d:\n", idx+1)
		testType, _ := test["testType"].(string)

		var result interface{}
		var runErr error

		switch testType {
		case "function":
			input := test["input"]
			functionName := test["functionName"]
			if functionName == nil {
				functionName = test["method"]
			}
			fname, _ := functionName.(string)
			fn, ok := exports[fname]
			if !ok {
				fmt.Println("  No exported function found; skipping execution")
			} else {
				rv := reflect.ValueOf(fn)
				if rv.Kind() != reflect.Func {
					fmt.Println("  Export is not a function; skipping")
				} else {
					args := toReflectArgs(input, rv.Type())
					out := rv.Call(args)
					if len(out) > 0 {
						result = out[0].Interface()
					}
				}
			}
		case "list":
			// build list and call solution(head)
			nodesRaw, _ := test["nodes"].([]interface{})
			nodes := toMapSlice(nodesRaw)
			headId, _ := test["headId"].(string)
			head, _ := algohelper.LoadList(nodes, headId)
			functionName := test["functionName"]
			fname, _ := functionName.(string)
			if fname == "" {
				if m, ok := test["method"].(string); ok {
					fname = m
				}
			}
			fn, ok := exports[fname]
			if ok {
				rv := reflect.ValueOf(fn)
				if rv.Kind() == reflect.Func {
					out := rv.Call([]reflect.Value{reflect.ValueOf(head)})
					if len(out) > 0 {
						result = out[0].Interface()
					}
				}
			} else {
				fmt.Println("  No exported function found for list test; skipping")
			}
		case "tree":
			treeRaw := test["tree"].(map[string]interface{})
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
			functionName := test["functionName"]
			fname, _ := functionName.(string)
			if fname == "" {
				if m, ok := test["method"].(string); ok {
					fname = m
				}
			}
			fn, ok := exports[fname]
			if ok {
				rv := reflect.ValueOf(fn)
				if rv.Kind() == reflect.Func {
					out := rv.Call([]reflect.Value{reflect.ValueOf(root)})
					if len(out) > 0 {
						result = out[0].Interface()
					}
				}
			} else {
				fmt.Println("  No exported function found for tree test; skipping")
			}
		case "graph":
			// For graph/class tests we expect an exported constructor in exports map
			graphRaw := test["graph"].(map[string]interface{})
			nodesRaw, _ := graphRaw["nodes"].([]interface{})
			nodes := toMapSlice(nodesRaw)
			startNodeId, _ := graphRaw["startNode"].(string)
			className, _ := test["className"].(string)
			methodName, _ := test["method"].(string)

			constructor, ok := exports[className]
			if !ok {
				fmt.Printf("  No exported constructor %s found; skipping graph test\n", className)
				break
			}
			// Build node instances by calling constructor(value)
			instances := map[string]reflect.Value{}
			ctor := reflect.ValueOf(constructor)
			for _, nd := range nodes {
				val := nd["value"]
				inst := ctor.Call([]reflect.Value{reflect.ValueOf(val)})
				instances[nd["id"].(string)] = inst[0]
			}
			// Attach children by calling AddChild (expects a node pointer)
			for _, nd := range nodes {
				id := nd["id"].(string)
				if children, ok := nd["children"].([]interface{}); ok {
					for _, ch := range children {
						cid := ch.(string)
						parent := instances[id]
						child := instances[cid]
						m := parent.MethodByName("AddChild")
						if m.IsValid() {
							m.Call([]reflect.Value{child})
						}
					}
				}
			}
			start := instances[startNodeId]
			// call the method
			m := start.MethodByName(upperFirst(methodName))
			if !m.IsValid() {
				fmt.Printf("  Method %s not found on class %s\n", methodName, className)
			} else {
				out := m.Call([]reflect.Value{reflect.ValueOf([]interface{}{})})
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
			fmt.Println("  Passed")
		} else {
			failed++
			fmt.Println("  Failed")
		}
		fmt.Printf("  Returned: %s\n", formatValue(result))
		fmt.Printf("  Expected: %s\n\n", formatValue(expected))

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

func upperFirst(s string) string {
	if s == "" {
		return s
	}
	return strings.ToUpper(s[:1]) + s[1:]
}

// toReflectArgs tries to convert the incoming JSON-like input into reflect.Values
// matching the function type `ft`.
func toReflectArgs(input interface{}, ft reflect.Type) []reflect.Value {
	var inputs []interface{}
	if input == nil {
		inputs = []interface{}{}
	} else {
		if arr, ok := input.([]interface{}); ok {
			inputs = arr
		} else {
			inputs = []interface{}{input}
		}
	}
	// build reflect.Values
	args := []reflect.Value{}
	for i := 0; i < ft.NumIn() && i < len(inputs); i++ {
		paramType := ft.In(i)
		rv := convertForType(inputs[i], paramType)
		args = append(args, rv)
	}
	return args
}

func convertForType(v interface{}, t reflect.Type) reflect.Value {
	// Basic conversions for common cases
	if v == nil {
		return reflect.Zero(t)
	}
	val := reflect.ValueOf(v)
	// Handle numeric JSON numbers (float64)
	if val.Kind() == reflect.Float64 {
		if t.Kind() >= reflect.Int && t.Kind() <= reflect.Int64 {
			return reflect.ValueOf(int(val.Float()))
		}
		if t.Kind() == reflect.Float64 {
			return reflect.ValueOf(val.Float())
		}
	}
	// If expected is slice or map and v is []interface{} or map[string]interface{},
	// pass as-is (caller function should accept interface{} and cast).
	if reflect.TypeOf(v).AssignableTo(t) {
		return reflect.ValueOf(v)
	}
	// Fallback: try to marshal and unmarshal into the desired type
	b, err := json.Marshal(v)
	if err == nil {
		ptr := reflect.New(t)
		if json.Unmarshal(b, ptr.Interface()) == nil {
			return ptr.Elem()
		}
	}
	return reflect.ValueOf(v)
}

func equals(a interface{}, b interface{}) bool {
	// Normalize both with JSON marshal/unmarshal so numerical types are comparable
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
