package algohelper

// Simple binary tree node used by the tests
type TreeNode struct {
	Value interface{}
	Left  *TreeNode
	Right *TreeNode
	Id    string
}

// BuildTree constructs TreeNode instances from test node data. nodeData is a
// slice of maps with keys: id, value, left (optional id), right (optional id).
// Returns the root node and a map of all nodes.
func BuildTree(nodeData []map[string]interface{}, rootId string) (*TreeNode, map[string]*TreeNode) {
	nodes := map[string]*TreeNode{}
	for _, it := range nodeData {
		id := it["id"].(string)
		nodes[id] = &TreeNode{Value: it["value"], Left: nil, Right: nil, Id: id}
	}
	for _, it := range nodeData {
		id := it["id"].(string)
		if left, ok := it["left"].(string); ok && left != "" {
			nodes[id].Left = nodes[left]
		}
		if right, ok := it["right"].(string); ok && right != "" {
			nodes[id].Right = nodes[right]
		}
	}
	return nodes[rootId], nodes
}
