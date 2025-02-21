/*
Binary Search Tree Height

Write a function that calculates the height of a Binary Search Tree (BST).
The height is the number of edges in the longest path from the root node to any leaf node.

What is tree height?
- Height is the maximum number of edges from root to leaf
- An empty tree has height of 0
- A tree with just a root node has height of 0
- A tree with root and one child has height of 1

Example Trees and Heights:

1. Height = 0          2. Height = 1          3. Height = 2
      10                    10                     10
                          /                      /    \
                         5                     5       15
                                              /
                                             2

4. Height = 3
      10
     /  \
    5    15
   / \     \
  2   7     20
             \
              25

Parameters:
- root: A BST node with properties:
  * value: number
  * left: BST node or null
  * right: BST node or null

Return:
- number: The height of the tree

Note:
- An empty tree (null root) should return 0
- A single node tree should return 0
- The height is the number of edges, not nodes
*/
function binarySearchTreeHeight(root) {
    if (!root) return 0;
    return 1 + Math.max(binarySearchTreeHeight(root.left), binarySearchTreeHeight(root.right));
}

module.exports = binarySearchTreeHeight;
