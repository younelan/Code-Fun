/*
Is Monotonic Array

Write a function that determines if an array is monotonic. An array is monotonic if it's either
monotonically increasing or monotonically decreasing.

What makes an array monotonic?
- Monotonically increasing: For all i <= j, array[i] <= array[j]
- Monotonically decreasing: For all i <= j, array[i] >= array[j]
- In other words, elements are always either non-increasing OR non-decreasing

Examples:

array = [1, 2, 3, 4, 4, 5]
returns: true (monotonically increasing)

array = [6, 5, 4, 4, 3, 1]
returns: true (monotonically decreasing)

array = [1, 1, 1, 1, 1, 1]
returns: true (both increasing and decreasing)

array = [1, 2, 1]
returns: false (increases then decreases)

Important Notes:
- An empty array or array of length 1 is monotonic
- Equal adjacent elements are valid in either direction
- The array can contain both positive and negative integers

Parameters:
- array: Array of integers

Return:
- boolean: true if the array is monotonic, false otherwise

Hints:
- Consider tracking the direction of change as you traverse the array
- Think about how to handle sequences of equal numbers
- You only need to check adjacent elements
*/

function isMonotonic(array) {
    // Write your code here
    return true;
}

module.exports = isMonotonic;
