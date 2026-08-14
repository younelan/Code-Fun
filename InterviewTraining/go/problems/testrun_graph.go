//go:build problem

package main

import (
	"fmt"
	"interviewtraining/algohelper"
	"os"
	"reflect"
)

// This runner is identical to testrun_local.go but includes support for
// graph/class-style tests by calling a constructor `New(value interface{}) interface{}`
// provided by the problem file compiled with this runner.

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: go run problems/testrun_graph.go <problemfile.go> -- <moduleName>")
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

		if testType == "" {
			if _, ok := test["input"]; ok {
				testType = "function"
			} else if _, aok := test["array"]; aok {
				testType = "function"
				test["input"] = []interface{}{test["array"], test["target"]}
			}
		}

		var result interface{}

		switch testType {
		case "function":
			input := test["input"]
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
		case "tree":
			treeRaw := test["tree"].(map[string]interface{})
			nodesRaw, _ := treeRaw["nodes"].([]interface{})
			nodes := toMapSlice(nodesRaw)
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
		case "graph":
			graphRaw := test["graph"].(map[string]interface{})
			nodesRaw, _ := graphRaw["nodes"].([]interface{})
			nodes := toMapSlice(nodesRaw)
			startNodeId, _ := graphRaw["startNode"].(string)
			className, _ := test["className"].(string)
			methodName, _ := test["method"].(string)

			// Constructor must be provided by the problem file: func New(value interface{}) interface{}
			ctor := reflect.ValueOf(New)
			instances := map[string]reflect.Value{}
			for _, nd := range nodes {
				val := nd["value"]
				inst := ctor.Call([]reflect.Value{reflect.ValueOf(val)})
				instances[nd["id"].(string)] = inst[0]
			}
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
			fmt.Printf("%s %s\n", prefix, algohelper.GetColorStr("Passed", "OKGREEN"))
		} else {
			failed++
			fmt.Printf("%s %s\n", prefix, algohelper.GetColorStr("Failed", "FAIL"))
			fmt.Printf("  Returned: %s\n", algohelper.GetColorStr(formatValue(result), "FAIL"))
			fmt.Printf("  Expected: %s\n\n", algohelper.GetColorStr(formatValue(expected), "OKGREEN"))
		}
	}

	total := passed + failed
	fmt.Printf("Total Tests: %d\nPassed: %d\nFailed: %d\n", total, passed, failed)
}

// Reuse helper functions from testrun_local.go by importing them via the same file
