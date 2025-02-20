/*
BST Traversal

You'll be implementing three different ways to walk through a binary search tree 
and collect all its values.

The tree you'll work with will be created like this:
const node10 = { value: 10, left: null, right: null };
const node5 = { value: 5, left: null, right: null };
const node15 = { value: 15, left: null, right: null };
const node2 = { value: 2, left: null, right: null };
const node7 = { value: 7, left: null, right: null };

// Connect the nodes to form:
//        10
//       /  \
//      5    15
//     / \
//    2   7

node10.left = node5;
node10.right = node15;
node5.left = node2;
node5.right = node7;

1. In-Order Traversal (inOrderTraverse):
    inOrderTraverse(node10, []) should return:
    [2, 5, 7, 10, 15]

2. Pre-Order Traversal (preOrderTraverse):
    preOrderTraverse(node10, []) should return:
    [10, 5, 2, 7, 15]

3. Post-Order Traversal (postOrderTraverse):
    postOrderTraverse(node10, []) should return:
    [2, 7, 5, 15, 10]

Your task:
Implement these three functions. Each should:
1. Take a BST node and an empty array as parameters
2. Add values to the array as you visit nodes
3. Return the array with all values in the correct order

Note: The actual tree in tests might be different, but will follow the same node structure:
{
    value: number,
    left: node | null,
    right: node | null
}
*/

function inOrderTraverse(tree, array) {
    // Write your code here
    return array;
}

function preOrderTraverse(tree, array) {
    // Write your code here
    return array;
}

function postOrderTraverse(tree, array) {
    // Write your code here
    return array;
}

module.exports = { inOrderTraverse, preOrderTraverse, postOrderTraverse };
