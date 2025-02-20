/*
Branch Sums

Write a function that takes in a Binary Tree and returns a list of its branch sums ordered from leftmost branch to rightmost branch.

What is a branch sum?
- A branch is a path of nodes from root to leaf
- A branch sum is the sum of all values in a branch
- A leaf node is a node with no children (no left or right nodes)

Example Tree:
        1
      /   \
     2     3
    / \   / \
   4   5 6   7
  / \  /
 8  9 10

Should return: [15, 16, 18, 16]
Explanation:
- 15 is from branch: 1 + 2 + 4 + 8
- 16 is from branch: 1 + 2 + 4 + 9
- 18 is from branch: 1 + 2 + 5 + 10
- 16 is from branch: 1 + 3 + 6

Note:
- Each BinaryTree node has an integer value, a left child node, and a right child node
- Children nodes can either be BinaryTree nodes themselves or None/null

Function info:
branchSums(root)
- Input: Root node of a binary tree
- Output: Array of branch sums from left to right

Sample Usage:
const root = new BinaryTree(1);
root.left = new BinaryTree(2);
root.right = new BinaryTree(3);
root.left.left = new BinaryTree(4);
root.left.right = new BinaryTree(5);
branchSums(root); // returns [7, 8, 4] (1+2+4, 1+2+5, 1+3)
*/

class BinaryTree {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

function branchSums(root, sums = [], curTotal = 0) {
    if (!root) return sums;

    curTotal += root.value;
    if (!root.left && !root.right) {
        sums.push(curTotal);
    }

    if (root.left) {
        branchSums(root.left, sums, curTotal);
    }
    if (root.right) {
        branchSums(root.right, sums, curTotal);
    }

    return sums;
}

module.exports = { BinaryTree, branchSums };
