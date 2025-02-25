/*
Validate Binary Search Tree

Write a function that determines if a binary tree is a valid binary search tree (BST).
A BST is valid if and only if all of its nodes satisfy the BST property.

The BST Property:
- Every node's value must be:
  * STRICTLY GREATER than ALL values in its left subtree
  * STRICTLY LESS than ALL values in its right subtree
- No duplicate values allowed

Example Valid BST:
       10
      /  \
     5    15
    / \   /
   2   7 13

Example Invalid BSTs:

1. Invalid because 15 in left subtree > 10:
       10
      /  \
     15   20

2. Invalid because 5 in right subtree < 10:
       10
      /  \
     3    5

3. Invalid because duplicate value 10:
       10
      /  \
     5    10

Parameters:
- tree: A binary tree node with properties:
  * value: integer
  * left: node or null
  * right: node or null
  * (you may also receive min/max bounds for recursive validation)

Return:
- boolean: true if tree is a valid BST, false otherwise

Hints:
- Think about using min/max bounds for each node
- Remember that ALL nodes in left subtree must be less than parent
- Remember that ALL nodes in right subtree must be greater than parent
*/

function validateBst(tree, minVal = -Infinity, maxVal = Infinity) {
    if (!tree) return true;
    if (tree.value < minVal || tree.value >= maxVal) return false;

    const leftValid = validateBst(tree.left, minVal, tree.value);
    const rightValid = validateBst(tree.right, tree.value, maxVal);

    return leftValid && rightValid;
}

module.exports = validateBst;
