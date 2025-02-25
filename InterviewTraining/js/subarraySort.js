/*
Subarray Sort Challenge

Imagine you have a partially sorted array, and you want to find out which section needs
to be sorted to make the entire array sorted. Your task is to find the smallest such section.

The Problem:
Given an array of numbers that's mostly sorted (but not completely), find:
1. Where does the unsorted section begin?
2. Where does the unsorted section end?

Step by Step Thinking:
1. First, identify what makes an array "sorted":
   - Each number should be greater than or equal to the previous number
   - Example sorted: [1, 2, 3, 4, 5]
   - Example not sorted: [1, 2, 5, 3, 4]

2. Look for numbers that are "out of place":
   - A number is out of place if it's:
     * Smaller than any number before it
     * Larger than any number after it

Examples:

Simple Example:
Input: [1, 2, 5, 3, 4, 6]
Output: [2, 4]
Why? The section [5, 3, 4] needs to be sorted:
- 5 is too large (should come after 3 and 4)
- 3 and 4 are too small (should come before 5)

Complex Example:
Input: [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
Output: [4, 9]
Walk through:
- First out of place: 7 (after 11)
- Last out of place: 7 (before 16)
- Must include 10, 11 because they're too large
- Must include 6 because it's too small
Therefore, subarray [10, 11, 7, 12, 6, 7] needs sorting

Already Sorted Example:
Input: [1, 2, 3, 4, 5]
Output: [-1, -1]
Why? Array is already sorted, so no subarray needs sorting

Expected Return:
- An array with two numbers: [startIndex, endIndex]
- If array is already sorted, return [-1, -1]

Tips:
- Consider edge cases (already sorted, completely reversed, duplicates)
- Think about how to identify numbers that are "out of place"
- The subarray might need to be larger than just the out-of-place numbers
*/

function subarraySort(array) {
    // Write your code here
    return [-1, -1];
}

module.exports = subarraySort;
