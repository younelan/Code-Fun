/*
Phone Number Mnemonics

Write a function that takes in a string representing a phone number and returns
all possible letter combinations that the phone number could represent based on
the old phone keypad mapping.

Phone Keypad Mapping:
1: "1"
2: "ABC"
3: "DEF"
4: "GHI"
5: "JKL"
6: "MNO"
7: "PQRS"
8: "TUV"
9: "WXYZ"
0: "0"

Examples:

Input: "43556"
Output includes: ["HELLO", "HELLO", "HELKM", ...]
Explanation:
- 4 maps to 'G', 'H', or 'I'
- 3 maps to 'D', 'E', or 'F'
- 5 maps to 'J', 'K', or 'L'
- 5 maps to 'J', 'K', or 'L'
- 6 maps to 'M', 'N', or 'O'
So "HELLO" is one of many possible combinations

Input: "23"
Output: ["AD", "AE", "AF", "BD", "BE", "BF", "CD", "CE", "CF"]
Explanation:
- 2 maps to 'A', 'B', or 'C'
- 3 maps to 'D', 'E', or 'F'

Parameters:
- phoneNumber: String containing digits from 0-9

Return:
- Array of strings representing all possible letter combinations

Notes:
- The digits 1 and 0 map to themselves
- The order of the combinations in the result array doesn't matter
- Each combination should be the same length as the input string
- Empty string returns empty array
- The input will only contain digits 0-9

Hints:
- Think about using recursion to build combinations
- Consider how to handle digits that map to different numbers of letters (like 7 and 9)
- You might want to store the keypad mapping in an object or array
*/

function phoneNumberMnemonics(phoneNumber) {
    // Digit to letters mapping
    const digitMap = {
        '0': ['0'],
        '1': ['1'],
        '2': ['A', 'B', 'C'],
        '3': ['D', 'E', 'F'],
        '4': ['G', 'H', 'I'],
        '5': ['J', 'K', 'L'],
        '6': ['M', 'N', 'O'],
        '7': ['P', 'Q', 'R', 'S'],
        '8': ['T', 'U', 'V'],
        '9': ['W', 'X', 'Y', 'Z']
    };
    
    const results = [];
    
    function backtrack(index, currentString) {
        // Base case: if we've processed all digits, add the combination
        if (index === phoneNumber.length) {
            results.push(currentString);
            return;
        }
        
        // Get current digit and its possible letters
        const currentDigit = phoneNumber[index];
        const letters = digitMap[currentDigit];
        
        // Try each possible letter for current digit
        for (const letter of letters) {
            backtrack(index + 1, currentString + letter);
        }
    }
    
    // Start the recursive process
    if (phoneNumber.length > 0) {
        backtrack(0, '');
    }
    
    return results;
}

module.exports = phoneNumberMnemonics;
