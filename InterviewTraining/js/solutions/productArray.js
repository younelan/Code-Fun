/*
Merge Overlapping Intervals

Write a function that takes in a non-empty array of arbitrary intervals and returns
an array of merged intervals. Each interval is an array of two integers, with
interval[0] as the start and interval[1] as the end.

What are intervals?
- Each interval represents a range of numbers
- Example: [1, 5] represents all numbers between 1 and 5 (inclusive)
- Intervals overlap if they share any numbers

Merging Rules:
- If two intervals overlap, they should be merged into one larger interval
- The merged interval should span from the lowest start to the highest end
- Non-overlapping intervals should remain separate
- The final array should be sorted by interval start times

Examples:

Input: [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
Output: [[1, 2], [3, 8], [9, 10]]
Explanation: [3, 5], [4, 7], and [6, 8] overlap, so they merge into [3, 8]

Input: [[1, 4], [4, 5], [2, 3]]
Output: [[1, 5]]
Explanation: All intervals overlap and merge into one

Input: [[1, 3], [2, 8], [9, 10]]
Output: [[1, 8], [9, 10]]
Explanation: First two intervals overlap

Parameters:
- intervals: Array of [start, end] arrays, where start and end are integers

Return:
- Array of merged [start, end] intervals

Note:
- Intervals are not necessarily sorted in the input
- An interval of [a, b] includes all numbers x where a ≤ x ≤ b
- Single-point intervals are valid (e.g., [1, 1])
*/
function arrayOfProducts(array) {
    const result = [];
    for (let i = 0; i < array.length; i++) {
        let product = 1;
        for (let j = 0; j < array.length; j++) {
            if (i !== j) {
                product *= array[j];
            }
        }
        result.push(product);
    }
    return result;
}

module.exports = arrayOfProducts;
