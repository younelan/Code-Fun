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
        if (value < this.value) {
            if (this.left === null) {
                this.left = new BST(value);
            } else {
                this.left.insert(value);
            }
        } else {
            if (this.right === null) {
                this.right = new BST(value);
            } else {
                this.right.insert(value);
            }
        }
        return this;
    }

    contains(value) {
        if (value === this.value) {
            return true;
        } else if (value < this.value) {
            return this.left ? this.left.contains(value) : false;
        } else {
            return this.right ? this.right.contains(value) : false;
        }
    }

    remove(value, parent = null) {
        if (value < this.value) {
            if (this.left) {
                this.left.remove(value, this);
            }
        } else if (value > this.value) {
            if (this.right) {
                this.right.remove(value, this);
            }
        } else {
            if (this.left && this.right) {
                this.value = this.right.getMinValue();
                this.right.remove(this.value, this);
            } else if (parent === null) {
                if (this.left) {
                    this.value = this.left.value;
                    this.right = this.left.right;
                    this.left = this.left.left;
                } else if (this.right) {
                    this.value = this.right.value;
                    this.left = this.right.left;
                    this.right = this.right.right;
                } else {
                    // Do nothing, this is a single-node tree; do not remove the root node.
                }
            } else if (parent.left === this) {
                parent.left = this.left ? this.left : this.right;
            } else if (parent.right === this) {
                parent.right = this.left ? this.left : this.right;
            }
        }
        return this;
    }

    getMinValue() {
        if (this.left === null) {
            return this.value;
        } else {
            return this.left.getMinValue();
        }
    }
}

module.exports = BST;
