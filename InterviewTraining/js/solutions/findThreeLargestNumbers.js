/*
Find Three Largest Numbers

Write a function that takes in an array of at least three integers and returns
a sorted array of the three largest integers in the input array.

Important Notes:
- The function should return duplicate integers if necessary
- For example, [10, 5, 9, 10, 12] should return [10, 10, 12]
- You're NOT allowed to sort the input array
- You should do this in one pass through the array

Examples:
array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
output = [18, 141, 541]

array = [55, 7, 8, 3, 43, 55, 67, 55]
output = [55, 55, 67]

array = [7, 7, 7, 7, 7, 7, 7]
output = [7, 7, 7]

Parameters:
- array: Array of at least 3 integers (can be positive or negative)

Return:
- Array of 3 integers, sorted in ascending order

Hints:
- Think about tracking the three largest numbers as you traverse the array
- Consider what happens when you find a number larger than your current largest
- Remember to shift the other numbers down when you find a larger one
*/

function findThreeLargestNumbers(array) {
    const retval = [Number.NEGATIVE_INFINITY, Number.NEGATIVE_INFINITY, Number.NEGATIVE_INFINITY];
    for (const val of array) {
        if (val > retval[2]) {
            retval[0] = retval[1];
            retval[1] = retval[2];
            retval[2] = val;
        } else if (val > retval[1]) {
            retval[0] = retval[1];
            retval[1] = val;
        } else if (val > retval[0]) {
            retval[0] = val;
        }
    }
    return retval;
}

module.exports = findThreeLargestNumbers;
