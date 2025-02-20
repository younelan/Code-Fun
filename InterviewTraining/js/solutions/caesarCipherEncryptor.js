/*
Caesar Cipher Encryptor

Named after Julius Caesar, who used it for secret military messages, the Caesar Cipher 
is one of the simplest and most widely known encryption techniques - it shifts each 
letter in the message by a fixed number of positions in the alphabet.

Write a function that takes in a non-empty string of lowercase letters and a non-negative integer key,
and returns a new string obtained by shifting every letter in the input string by k positions in the alphabet.

The cipher should "wrap around" the alphabet. For example, the letter 'z' shifted by 2 becomes 'b'.

Examples:
string = "wxy"
key = 2
result = "yza"

string = "abc"
key = 3
result = "def"

string = "abc"
key = 52
result = "abc"  (because 52 positions is the same as 0 positions as 52 % 26 = 0)

Parameters:
- string: A string of lowercase letters (a-z)
- key: A non-negative integer

Important Notes:
- The string will only contain lowercase letters (no numbers, symbols, spaces)
- The key can be any non-negative integer (handle cases where key > 26)
- You'll need to handle "wrapping" around the alphabet
- Consider using ASCII values (a = 97, z = 122)
- Remember to handle cases where key is larger than 26 (use modulo)

Return:
- A string with each character shifted by 'key' positions
*/
function caesarCipherEncryptor(string, key) {
    if (key > 25) {
        key = key % 26;
    }
    let retval = "";
    for (const ch of string) {
        const newval = "a".charCodeAt(0) + (ch.charCodeAt(0) - "a".charCodeAt(0) + key) % 26;
        retval += String.fromCharCode(newval);
    }
    return retval;
}

module.exports = caesarCipherEncryptor;
