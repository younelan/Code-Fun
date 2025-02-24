/*
Minimum Height BST

Write a function that takes in a non-empty sorted array of distinct integers and
constructs a BST of minimum height using those integers.

What is a minimum height BST?
- A Binary Search Tree where the difference between heights of left and right subtrees
  for every node is not more than 1
- In other words, it's a balanced BST
- The height should be as small as possible

Example:
Input: [1, 2, 5, 7, 10, 13, 14, 15, 22]

Should create:
         10
       /    \
      2      14
     / \    /  \
    1   5  13   15
         \        \
          7        22

Note: Other valid minimum-height BSTs can be constructed from the input.

Sample Usage:
const bst = minHeightBst([1, 2, 5, 7, 10, 13, 14, 15, 22])
bst.left.value // 2
bst.right.value // 14
bst.value // 10

Important Notes:
- The input array will be sorted in ascending order
- The array will contain distinct integers (no duplicates)
- Use the provided BST class
- Think about using the middle element as root

Parameters:
- array: Sorted array of distinct integers

Return:
- The root node of the minimum height BST

Hints:
- Consider using binary search concepts
- The middle element should be the root
- Recursively build left and right subtrees

Common Mistake Example:
Input array: [1, 2, 3, 4, 5, 6, 7]

Wrong Implementation (creates unbalanced tree):
        1
         \
          2
           \
            3
             \
              4
               \
                5
                 \
                  6
                   \
                    7

Height: 6 (too tall!)

Correct Implementation (balanced tree):
            4
         /     \
        2       6
       / \     / \
      1   3   5   7

Height: 2 (minimum possible!)

Why the first implementation fails:
- Simply inserting elements in order creates a linked list
- Each node only has a right child
- Height becomes O(n) instead of O(log n)
- Not utilizing the fact that the input array is sorted
- Doesn't pick middle elements as roots

Remember:
- Always use the middle element as the root for each subtree
- Recursively build left and right subtrees using remaining elements
- This ensures the tree remains balanced
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
    }
}

function minHeightBst(input) {
    // Input from genericRunner comes as first element of array
    const array = Array.isArray(input) ? input : [input];
    
    if (!array || array.length === 0) return null;
    
    function buildBST(start, end) {
        if (start > end) return null;
        
        const mid = Math.floor((start + end) / 2);
        const node = new BST(array[mid]);
        
        node.left = buildBST(start, mid - 1);
        node.right = buildBST(mid + 1, end);
        
        return node;
    }
    
    const sortedArray = array.slice().sort((a, b) => a - b);
    return buildBST(0, sortedArray.length - 1);
}

module.exports = minHeightBst;
