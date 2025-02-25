/*
Spiral Traverse

Write a function that takes in a two-dimensional array and returns a one-dimensional
array containing all elements in spiral order.

What is Spiral Order?
- Start at top left corner
- Move right to the end of the row
- Move down to the end of the column
- Move left to the start of the row
- Move up to the start of the column
- Repeat inward until all elements are visited

Example:
array = [
    [1,  2,  3,  4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9,  8,  7]
]

Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

Visual of the spiral path:
→ → → →
      ↓
↑     ↓
↑     ↓
↑ ← ← ↓

Another Example:
array = [
    [1, 2, 3],
    [8, 9, 4],
    [7, 6, 5]
]
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

Parameters:
- array: 2D array of integers

Return:
- 1D array of integers in spiral order

Edge Cases:
- Single row matrix
- Single column matrix
- Empty matrix
- Non-square matrix
*/

function spiralTraverse(array) {
    // Write your code here
    const result = [];
    return result;
}

module.exports = spiralTraverse;
