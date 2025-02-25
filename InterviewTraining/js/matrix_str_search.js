/*
Matrix String Search (Word Search)

Write a function that takes in a 2D array of letters (matrix) and a string to find.
Return [true, direction] if the string is found in the matrix, [false, ""] if not.
The word can be found in any of six directions: "north", "south", "east", "west",
"south-east", or "south-west".

The Challenge:
- Search for a string in a 2D matrix
- Words can be found in 6 different directions
- Return both whether the word was found and in which direction

Example Matrix:
[
    ["A", "B", "C", "D"],
    ["E", "F", "G", "H"],
    ["I", "J", "K", "L"],
    ["M", "N", "O", "P"]
]

Example Test Cases:
matrix_search(matrix, "CFG") // returns [true, "east"]
matrix_search(matrix, "AIM") // returns [true, "south"]
matrix_search(matrix, "FL") // returns [true, "south-east"]
matrix_search(matrix, "XYZ") // returns [false, ""]

Sample Usage:
const matrix = [
    ["H", "E", "L", "L", "O"],
    ["E", "L", "L", "O", "T"],
    ["Y", "E", "S", "!", "O"],
    ["W", "O", "R", "L", "D"]
    ];
matrix_search(matrix, "HELLO") // returns [true, "east"]

Parameters:
- M: 2D array of single characters (the matrix)
- S: String to search for

Return:
- Array containing:
  * boolean: whether the string was found
  * string: direction of the word (one of the six directions, or empty string if not found)

Notes:
- The word must be found in exact sequence
- All characters will be uppercase letters
- The matrix will always be rectangular (all rows same length)
- Valid directions are: "north", "south", "east", "west", "south-east", "south-west"
*/

function matrix_search(M, S) {
    // Write your code here
    return [false, ""];
}

function full_word_search(M, startX, startY, target) {
    // Write your helper function here
    // This function checks all possible directions from a starting point
    return [false, ""];
}

module.exports = matrix_search;
