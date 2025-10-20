package algohelper

import "fmt"

type ListNode struct {
	Value interface{}
	Next  *ListNode
	Id    string
}

// LoadList builds linked list nodes from the test representation. `nodesData`
// is a slice of maps with keys: id, value, next (optional id).
// headId selects the id for the head node to return.
func LoadList(nodesData []map[string]interface{}, headId string) (*ListNode, map[string]*ListNode) {
	items := map[string]*ListNode{}
	for _, it := range nodesData {
		id := it["id"].(string)
		items[id] = &ListNode{Value: it["value"], Next: nil, Id: id}
	}
	for _, it := range nodesData {
		id := it["id"].(string)
		if next, ok := it["next"].(string); ok && next != "" {
			items[id].Next = items[next]
		}
	}
	return items[headId], items
}

// GetListStr returns a simple string representation for printing.
func GetListStr(head *ListNode) string {
	var parts []string
	for n := head; n != nil; n = n.Next {
		parts = append(parts, fmtString(n.Value))
	}
	return "[" + join(parts, ", ") + "]"
}

// small helpers to avoid importing fmt/strings everywhere
func fmtString(v interface{}) string {
	if v == nil {
		return "null"
	}
	return fmt.Sprintf("%v", v)
}

func join(arr []string, sep string) string {
	if len(arr) == 0 {
		return ""
	}
	s := arr[0]
	for i := 1; i < len(arr); i++ {
		s += sep + arr[i]
	}
	return s
}
