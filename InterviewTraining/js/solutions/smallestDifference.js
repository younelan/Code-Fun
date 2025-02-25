/*
Smallest Difference

Write a function that takes in two non-empty arrays of integers and finds the
pair of numbers (one from each array) whose absolute difference is closest to zero.

The Problem:
- Find one number from first array and one from second array
- Calculate their absolute difference |num1 - num2|
- Return the pair with the smallest difference
- If multiple pairs have same difference, return any one of them

Examples:
arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]
Returns: [28, 26]  
// Difference is 2, which is smallest possible

arrayOne = [10, 0, 20, 25]
arrayTwo = [1005, 1006, 1014, 1032, 1031]
Returns: [25, 1005]  
// Difference of 980 is smallest possible

arrayOne = [240, 124, 86, 111, 2, 84, 954, 27, 89]
arrayTwo = [1, 3, 954, 19, 8]
Returns: [954, 954]  
// Perfect match, difference is 0

Parameters:
- arrayOne: Non-empty array of integers
- arrayTwo: Non-empty array of integers

Return:
- Array of two integers [num1, num2] where:
  * num1 is from arrayOne
  * num2 is from arrayTwo
  * |num1 - num2| is minimal

Notes:
- Arrays won't be empty
- There will always be a valid answer
- Return array should maintain order (first number from first array)
*/

function smallestDifference(arrayOne, arrayTwo) {
    let minDiff = Infinity;
    let result = [];
    for (let i = 0; i < arrayOne.length; i++) {
        for (let j = 0; j < arrayTwo.length; j++) {
            const diff = Math.abs(arrayOne[i] - arrayTwo[j]);
            if (diff < minDiff) {
                minDiff = diff;
                result = [arrayOne[i], arrayTwo[j]];
            }
        }
    }
    return result;
}

module.exports = smallestDifference;
