/*
Given an array of integers, find all triplets in the array that sum up to a given target sum.

Problem:
- Input: An array of integers and a target sum
- Output: Array of all triplets that sum to target
- Triplets should be sorted in ascending order
- Each triplet should contain unique numbers
- The function should return an empty array if no triplets are found

Example:
array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0

Output: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

Time Complexity: O(n³) - using three nested loops
Space Complexity: O(n) - where n is the number of triplets found
*/

function threeNumberSum(array, targetSum) {
    const arrSorted = array.slice().sort((a, b) => a - b);
    const retval = [];
    for (let i = 0; i < arrSorted.length - 2; i++) {
        for (let j = i + 1; j < arrSorted.length - 1; j++) {
            for (let k = j + 1; k < arrSorted.length; k++) {
                if (arrSorted[i] + arrSorted[j] + arrSorted[k] === targetSum) {
                    retval.push([arrSorted[i], arrSorted[j], arrSorted[k]]);
                }
            }
        }
    }
    return retval;
}

module.exports = threeNumberSum;
