/*
First Duplicate Value

Given an array of integers between 1 and n, where n is the length of the array,
write a function that returns the first integer that appears more than once when reading from left to right.

Rules:
- If no integer appears more than once, return -1
- The input array will always be valid (integers between 1 and array length)
- You're looking for the first VALUE that appears twice, not the first position where a duplicate occurs

Examples:
array = [2, 1, 5, 2, 3, 3, 4]
returns: 2 (2 is the first value that appears twice)

array = [2, 1, 5, 3, 3, 2, 4]
returns: 3 (while 2 appears twice, 3 is the first value to appear twice)

array = [1, 2, 3, 4, 5, 6]
returns: -1 (no duplicates exist)

Parameters:
- array: Array of integers where each integer is between 1 and array.length

Return:
- The first value that appears twice, or -1 if no value appears twice

Hints:
- Consider using a hash table/object to track seen values
- Think about how to handle the case where no duplicates exist
*/

function firstDuplicateValue(array) {
    const counts = {};
    for (const el of array) {
        counts[el] = (counts[el] || 0) + 1;
        if (counts[el] > 1) {
            return el;
        }
    }
    return -1;
}

module.exports = firstDuplicateValue;
