/*
Binary Search Tree Implementation

You need to implement four methods that work with a Binary Search Tree (BST).
Each node in the tree has three properties:
- value: The number stored in the node
- left: Reference to left child (or null)
- right: Reference to right child (or null)

1. insert(value) Method:
   - Takes a number as input
   - Adds it to the BST following these rules:
     * If value < node.value, go to left subtree
     * If value >= node.value, go to right subtree
     * Place new node when you find an empty spot (null)
   - Returns the BST object for chaining
   Example:
   bst.insert(5) creates:
        10
       /
      5

2. contains(value) Method:
   - Takes a number as input
   - Returns true if that number exists in the tree, false otherwise
   - Follow BST rules to search:
     * If value === node.value, found it!
     * If value < node.value, search left subtree
     * If value > node.value, search right subtree
   Example:
   bst.contains(5) returns true
   bst.contains(8) returns false

3. remove(value) Method:
   - Takes a number as input
   - Removes that number from tree if it exists
   - Must handle three cases:
     * Removing leaf node (no children)
     * Removing node with one child
     * Removing node with two children (replace with smallest value from right subtree)
   - Returns the BST object
   Example:
   Starting with:    Removing 5:
        10               10
       /  \             /  \
      5    15    =>    7    15
     / \               /
    2   7             2

4. getMinValue() Method:
   - Helper method used by remove()
   - Returns the smallest value in current subtree
   - Implementation hint: Keep going left until you can't anymore

Example Usage:
const bst = new BST(10);
bst.insert(5).insert(15);    // Returns the BST after each insert
bst.contains(5);             // Returns true
bst.contains(8);             // Returns false
bst.remove(5);              // Returns the BST
*/

class BST {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }

    insert(value) {
        // Write your code here
        // Return this BST
        return this;
    }

    contains(value) {
        // Write your code here
        // Return true if value exists in the BST, false otherwise
        return false;
    }

    remove(value, parent = null) {
        // Write your code here
        // Return this BST
        return this;
    }

    getMinValue() {
        // Write your code here
        // Helper method for remove
        // Return the minimum value in this subtree
        return 0;
    }
}

module.exports = BST;
