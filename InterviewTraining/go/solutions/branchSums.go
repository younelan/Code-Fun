//go:build problem

package main

// Binary tree node for branch sums
type TreeNode struct {
    Value int
    Left  *TreeNode
    Right *TreeNode
}

// BranchSums computes the sums of each root-to-leaf path
func BranchSums(root *TreeNode) []int {
    var res []int
    var dfs func(node *TreeNode, sum int)
    dfs = func(node *TreeNode, sum int) {
        if node == nil {
            return
        }
        sum += node.Value
        if node.Left == nil && node.Right == nil {
            res = append(res, sum)
            return
        }
        dfs(node.Left, sum)
        dfs(node.Right, sum)
    }
    dfs(root, 0)
    return res
}

// Solution wrapper
func Solution(root *TreeNode) []int {
    return BranchSums(root)
}
