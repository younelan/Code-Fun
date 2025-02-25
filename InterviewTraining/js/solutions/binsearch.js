/*
Binary Search

Write a function that takes in a sorted array of integers and a target integer,
and returns the index of the target integer in the array. If the target isn't
found in the array, return -1.

The Binary Search Process:
1. Find the middle element of the array
2. If target equals middle element, we found it!
3. If target < middle element, search left half
4. If target > middle element, search right half
5. Repeat until target is found or determined to not exist

Examples:

Input: array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
       target = 33
Output: 3
Explanation: 33 is at index 3

Input: array = [1, 5, 23, 111]
       target = 111
Output: 3
Explanation: 111 is at index 3

Input: array = [1, 5, 23, 111]
       target = 35
Output: -1
Explanation: 35 isn't in the array

Important Notes:
- Array will always be sorted in ascending order
- Array may contain duplicate values
- Time complexity should be O(log n)
- Space complexity should be O(1)

Hints:
- Think about how to efficiently eliminate half of the remaining elements each time
- Keep track of the search boundaries
- Consider how to handle duplicates
*/

function binarySearch(array, target) {
    let left = 0;
    let right = array.length - 1;
    
    while (left <= right) {
        // Calculate middle index
        // Using (left + right) / 2 can cause integer overflow
        // This formula is safer
        const mid = left + Math.floor((right - left) / 2);
        
        // Found the target
        if (array[mid] === target) {
            return mid;
        }
        
        // Target is in left half
        if (target < array[mid]) {
            right = mid - 1;
        }
        // Target is in right half
        else {
            left = mid + 1;
        }
    }
    
    // Target not found
    return -1;
}

module.exports = binarySearch;
