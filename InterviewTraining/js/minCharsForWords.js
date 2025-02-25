/*
Minimum Characters For Words

Write a function that takes in an array of words and returns the smallest array of
characters needed to form all the words.

The Problem:
- Given an array of words, find the minimum set of characters needed to construct all words
- Each character in the output can be used multiple times
- The characters can be returned in any order
- Think of it as finding the minimum set of Scrabble tiles needed

Examples:

Input: ["this", "that", "did", "deed", "them!"]
Output: ["t", "t", "h", "i", "s", "a", "d", "d", "e", "e", "m", "!"]
Explanation:
- We need two 't's because "this" and "that" both need a 't'
- We need two 'd's because "deed" needs two 'd's
- We need two 'e's because "deed" needs two 'e's
- Every other character appears at most once in any word

Input: ["cat", "bat", "tab"]
Output: ["c", "a", "t", "b"]
Explanation:
- We only need one of each letter because no word uses the same letter twice
- Order doesn't matter in the output

Input: ["ball", "call", "tall"]
Output: ["b", "a", "l", "l", "c", "t"]
Explanation:
- We need two 'l's because "ball" needs two 'l's
- One of each other character is sufficient

Parameters:
- words: Array of strings

Return:
- Array a sorted array of characters (strings of length 1)

Hints:
- Consider using a frequency counter for each word
- Think about how to track the maximum frequency of each character across all words
- Remember that you need enough characters for any single word
*/

function minimumCharactersForWords(words) {
    const result = [];    
    return result.sort();
}

module.exports = minimumCharactersForWords;
