//go:build problem

package main

// BSTNode implements insert/contains/remove/getMinValue
type BSTNode struct {
    Value int
    Left  *BSTNode
    Right *BSTNode
}

func (b *BSTNode) Insert(value int) *BSTNode {
    if value < b.Value {
        if b.Left == nil {
            b.Left = &BSTNode{Value: value}
        } else {
            b.Left.Insert(value)
        }
    } else {
        if b.Right == nil {
            b.Right = &BSTNode{Value: value}
        } else {
            b.Right.Insert(value)
        }
    }
    return b
}

func (b *BSTNode) Contains(value int) bool {
    if b == nil {
        return false
    }
    if value < b.Value {
        return b.Left != nil && b.Left.Contains(value)
    } else if value > b.Value {
        return b.Right != nil && b.Right.Contains(value)
    }
    return true
}

func (b *BSTNode) GetMinValue() int {
    curr := b
    for curr.Left != nil {
        curr = curr.Left
    }
    return curr.Value
}

// Remove returns the node (root may change) after removing value
func (b *BSTNode) Remove(value int) *BSTNode {
    if b == nil {
        return nil
    }
    if value < b.Value {
        b.Left = b.Left.Remove(value)
    } else if value > b.Value {
        b.Right = b.Right.Remove(value)
    } else {
        // found node
        if b.Left == nil && b.Right == nil {
            return nil
        }
        if b.Left == nil {
            return b.Right
        }
        if b.Right == nil {
            return b.Left
        }
        // two children: replace with min from right subtree
        minVal := b.Right.GetMinValue()
        b.Value = minVal
        b.Right = b.Right.Remove(minVal)
    }
    return b
}

// Solution wrapper: accepts either a root BSTNode or operations — implement basic API
func Solution(root *BSTNode, action string, value int) interface{} {
    switch action {
    case "insert":
        if root == nil {
            return &BSTNode{Value: value}
        }
        root.Insert(value)
        return root
    case "contains":
        if root == nil {
            return false
        }
        return root.Contains(value)
    case "remove":
        if root == nil {
            return root
        }
        return root.Remove(value)
    default:
        return root
    }
}
