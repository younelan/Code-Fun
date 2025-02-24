/*
Run Length Encoding

Write a function that takes in a non-empty string and returns its run-length encoding.
Run-length encoding is a form of lossless data compression where consecutive data elements
are stored as a single value and count, rather than as the original run.

Rules:
1. Encode consecutive repeated characters with their count followed by the character
2. If a character repeats more than 9 times, split it into multiple encodings
3. All characters in input string will be uppercase letters, no numbers

Examples:

Input: "AAAAAAAAAAAAAABBCCCC"
Output: "9A4A2B4C"
Explanation:
- First 13 A's become "9A4A" (split because count > 9)
- 2 B's become "2B"
- 4 C's become "4C"

Input: "WWWWWWWWWWWWBWWWWWWWWWWWW"
Output: "9W3W1B9W4W"
Explanation:
- First 12 W's become "9W3W"
- Single B becomes "1B"
- Last 13 W's become "9W4W"

Input: "  hsqq qww  "
Output: "2 1h1s2q1 2w2 "
Explanation:
- Even spaces are encoded with their count

Parameters:
- string: A non-empty string

Return:
- The run-length encoded string

Note:
- You must handle counts greater than 9 by splitting them
- Every character should be encoded, even if count is 1
- Spaces should be encoded just like any other character
*/

function runLengthEncoding(string) {
    let counter = 1;
    let prevChar = string[0];
    let result = "";
    for (let i = 1; i < string.length; i++) {
        const char = string[i];
        if (char === prevChar) {
            counter++;
            if (counter > 9) {
                result += "9" + char;
                counter = 1;
            }
        } else {
            result += counter + prevChar;
            prevChar = char;
            counter = 1;
        }
    }
    result += counter + prevChar;
    return result;
}

module.exports = runLengthEncoding;
