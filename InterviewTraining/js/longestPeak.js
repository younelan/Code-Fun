/*
Longest Peak

Write a function that takes in an array of integers and returns the length of the longest peak in the array.

What is a peak?
- A peak is a sequence of consecutive integers that are:
  * Strictly increasing until they reach the highest value (the peak)
  * Then strictly decreasing after the highest value
- Must have at least 3 numbers to form a peak
- The peak is the highest point in the sequence

Examples of peaks:
[1, 4, 10, 2]     // Valid peak of length 4
[2, 3, 6, 5, 4]   // Valid peak of length 5
[1, 2, 2, 3]      // Not a peak (not strictly increasing)
[1, 2, 3]         // Not a peak (no decreasing part)
[1, 2, 3, 3, 2]   // Not a peak (not strictly decreasing)

Sample Input:
array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]

Sample Output:
6  // The peak 0, 10, 6, 5, -1, -3

Parameters:
- array: Array of integers

Return:
- Length of the longest peak (integer)
- Return 0 if no peak exists

Notes:
- Peak must be strictly increasing then strictly decreasing
- A peak must have at least 3 elements
- Peaks don't overlap, but can share edges ([1,4,5,2,7,8,4] has two peaks)
*/

function longestPeak(array) {
    // Write your code here
    return 0;
}

module.exports = longestPeak;
