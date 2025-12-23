//go:build problem

package main

// Original JS: js/bstInsertRemove.js
// Provide a BST type with Insert and Remove methods. The runner can call
// `New(value)` to construct nodes for class-style tests.

type BST struct {
	Value int
	Left  *BST
	Right *BST
}

func (b *BST) Insert(value int) *BST {
	// TODO: implement insertion
	return b
}

func (b *BST) Remove(value int) *BST {
	// TODO: implement removal
	return b
}

func New(value interface{}) interface{} {
	v, _ := value.(float64)
	return &BST{Value: int(v)}
}

// Dummy Solution to satisfy testrun_local.go references; class behavior uses New and methods.
func Solution(input interface{}) interface{} {
	return nil
}
