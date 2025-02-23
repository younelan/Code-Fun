/*
Array of Products

Write a function that takes in an array of integers and returns an array of the same
length, where each element in the output array is equal to the product of every other
number in the input array.

In other words, the value at output[i] is equal to the product of every number in the
input array other than input[i].

Important Notes:
- You can't use division in your solution
- The output array should be the same length as the input array
- You should not include the number at the current index in the product

Examples:
Input:  [5, 1, 4, 2]
Output: [8, 40, 10, 20]
// 8  is 1 x 4 x 2
// 40 is 5 x 4 x 2
// 10 is 5 x 1 x 2
// 20 is 5 x 1 x 4

Input:  [1, 8, 6, 2, 4]
Output: [384, 48, 64, 192, 96]
// 384 is 8 x 6 x 2 x 4
// 48  is 1 x 6 x 2 x 4
// 64  is 1 x 8 x 2 x 4
// 192 is 1 x 8 x 6 x 4
// 96  is 1 x 8 x 6 x 2

Parameters:
- array: Non-empty array of integers

Return:
- Array of products (excluding current index)

Constraints:
- Don't use division
- Handle edge cases (array of length 1)
- Handle zeros in the input array
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
