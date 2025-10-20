package algohelper

import (
	"reflect"
)

// Simple graph loader: nodes represented as maps in tests are expected to have
// an `id`, `value`, and `children` array of ids.

type GraphNode struct {
	Value    interface{}
	Children []*GraphNode
}

// LoadGraph constructs nodes and links using the provided node data.
// nodesData is expected to be a slice of maps with keys: id, value, children ([]interface{} ids).
func LoadGraph(nodesData []map[string]interface{}, startNodeId string) (*GraphNode, map[string]*GraphNode) {
	nodes := map[string]*GraphNode{}
	for _, data := range nodesData {
		id := data["id"].(string)
		nodes[id] = &GraphNode{Value: data["value"], Children: []*GraphNode{}}
	}
	for _, data := range nodesData {
		id := data["id"].(string)
		if children, ok := data["children"].([]interface{}); ok {
			for _, ch := range children {
				cid := ch.(string)
				nodes[id].Children = append(nodes[id].Children, nodes[cid])
			}
		}
	}
	return nodes[startNodeId], nodes
}

// InstantiateGraph builds problem-specific instances by calling the provided
// constructor function `ctor` for each node value. `ctor` must be a function
// with signature `func(value interface{}) interface{}` returning an instance.
// Returns a map[id]reflect.Value for the created instances.
func InstantiateGraph(nodesData []map[string]interface{}, ctor interface{}) (map[string]reflect.Value, error) {
	instances := map[string]reflect.Value{}
	cval := reflect.ValueOf(ctor)
	for _, data := range nodesData {
		id := data["id"].(string)
		val := data["value"]
		out := cval.Call([]reflect.Value{reflect.ValueOf(val)})
		if len(out) > 0 {
			v := out[0]
			// If constructor returns an interface{}, unwrap to the concrete value
			if v.Kind() == reflect.Interface && v.Elem().IsValid() {
				v = v.Elem()
			}
			instances[id] = v
		} else {
			instances[id] = reflect.Value{}
		}
	}
	return instances, nil
}

// AttachChildren connects instances based on `children` fields in nodesData.
// It expects instances to be a map[id]reflect.Value. Each parent will be
// called with its `AddChild` method passing the child instance.
func AttachChildren(instances map[string]reflect.Value, nodesData []map[string]interface{}) error {
	for _, data := range nodesData {
		id := data["id"].(string)
		if children, ok := data["children"].([]interface{}); ok {
			parent := instances[id]
			if parent.Kind() == reflect.Interface && parent.Elem().IsValid() {
				parent = parent.Elem()
			}
			for _, ch := range children {
				cid := ch.(string)
				child := instances[cid]
				if child.Kind() == reflect.Interface && child.Elem().IsValid() {
					child = child.Elem()
				}
				if !parent.IsValid() || !child.IsValid() {
					continue
				}
				m := parent.MethodByName("AddChild")
				if m.IsValid() {
					m.Call([]reflect.Value{child})
				}
			}
		}
	}
	return nil
}
