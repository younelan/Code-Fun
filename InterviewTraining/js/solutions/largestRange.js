/*
Largest Range

Write a function that takes in an array of integers and returns an array of length 2
representing the largest range of consecutive integers contained in that array.

What is a Range?
- A range is a set of consecutive integers
- For example, [1, 2, 3, 4] is a range of length 4
- The numbers don't need to appear consecutively in the input array
- Each number in the input array can only be used once in a range

Examples:

Input: [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
Output: [0, 7]
Explanation:
- The numbers 0, 1, 2, 3, 4, 5, 6, 7 form a consecutive range
- This is the largest such range in the array
- The range [10, 11, 12] exists but is smaller

Input: [1, 1, 1, 3, 4]
Output: [3, 4]
Explanation:
- Duplicate numbers can only be used once
- [3, 4] is the largest range

Input: [4, 2, 1, 3]
Output: [1, 4]
Explanation:
- Even though numbers aren't sequential in array
- They form a consecutive range when sorted

Parameters:
- array: Array of integers (may contain duplicates)

Return:
- Array of two integers [start, end] representing the smallest and largest numbers
  in the longest range of consecutive integers found

Notes:
- A single number counts as a range of length 1
- Numbers don't need to be adjacent in the input array to form a range
- You can assume there will always be at least one number in the input array
*/

function largestRange(array) {
    const arr = array.slice().sort((a, b) => a - b);
    if (arr.length === 1) return [arr[0], arr[0]];
    if (arr.length === 2) return arr;

    let first = arr.shift();
    let prev = first;
    let last = first;
    let minval = first;
    let maxval = first;
    let count = 0;

    while (arr.length) {
        const cur = arr.shift();
        if (cur === prev) continue;
        if (prev + 1 === cur) {
            count++;
            last = cur;
            if (last - first > maxval - minval) {
                minval = first;
                maxval = last;
            }
        } else {
            first = cur;
            count = 1;
        }
        prev = cur;
    }
    return [minval, maxval];
}

module.exports = largestRange;
