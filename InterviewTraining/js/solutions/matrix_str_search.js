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

Example Searches:
1. Search for "CFG":
   - Found: true
   - Direction: "east"
   - Location: starts at C, goes right

2. Search for "AIM":
   - Found: true
   - Direction: "south"
   - Location: starts at A, goes down

3. Search for "FL":
   - Found: true
   - Direction: "south-east"
   - Location: starts at F, goes diagonally down-right

Parameters:
- M: 2D array of single characters (the matrix)
- S: String to search for

Return:
- Array containing:
  * boolean: whether the string was found
  * string: direction of the word ("north", "south", "east", "west", "south-east", "south-west")
  * empty string if word not found

Notes:
- The word must be found in exact sequence
- All characters will be uppercase letters
- The matrix will always be rectangular (all rows same length)
*/

function matrix_search(M, S) {
    const width = M[0].length;
    const height = M.length;
    for (let x = 0; x < width; x++) {
        for (let y = 0; y < height; y++) {
            if (M[y][x] === S[0]) {
                const [found, direction] = full_word_search(M, x, y, S);
                if (found) {
                    return [true, direction];
                }
            }
        }
    }
    return [false, ""];
}

function full_word_search(M, startX, startY, target) {
    const width = M[0].length;
    const height = M.length;
    const searchParams = [
        [1, 1, "south-east"], [-1, -1, "south-west"], [1, 0, "south"],
        [0, 1, "east"], [0, -1, "west"], [-1, 0, "north"]
    ];

    for (const [dx, dy, direction] of searchParams) {
        let idx = 0;
        let col = startX;
        let row = startY;
        const tLength = target.length;
        while (row >= 0 && col >= 0 && col < width && row < height && M[row][col] === target[idx]) {
            idx++;
            row += dx;
            col += dy;
            if (idx === tLength) {
                return [true, direction];
            }
        }
    }
    return [false, ""];
}

module.exports = matrix_search;
