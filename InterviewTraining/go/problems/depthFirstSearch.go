//go:build problem

package main

/*
Original JS: js/depthFirstSearch.js

This file defines a Node type with a DepthFirstSearch method.
The runner expects a constructor-style symbol `New(value interface{}) interface{}`
that returns a *Node so it can instantiate nodes during tests.
*/

type Node struct {
	Name     string
	Children []*Node
}

func (n *Node) AddChild(child *Node) *Node {
	n.Children = append(n.Children, child)
	return n
}

// DepthFirstSearch performs DFS and returns a slice of visited names.
// TODO: implement traversal logic.
func (n *Node) DepthFirstSearch(arr []interface{}) []interface{} {
	return nil
}

// New constructs a Node instance from a test value (usually a string name).
func New(value interface{}) interface{} {
	name, _ := value.(string)
	return &Node{Name: name, Children: []*Node{}}
}

// Provide a no-op Solution stub so the local runner can compile this file
// even though depthFirstSearch is exercised as a graph/class test.
func Solution(input interface{}) interface{} {
	return nil
}
