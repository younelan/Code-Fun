/*
Generate Valid IP Addresses

You're given a string of digits. Write a function that returns all possible valid IP address combinations
that can be created by inserting three dots (.) in the string.

What makes a valid IP address?
- Consists of 4 parts separated by dots
- Each part must be a number between 0 and 255
- No part can have leading zeros unless it's a single zero (0 is valid, 00 is not)

Example:
Input: "1921680"
Output: [
    "1.9.216.80",
    "1.92.16.80",
    "1.92.168.0",
    "19.2.16.80",
    "19.2.168.0",
    "19.21.6.80",
    "19.21.68.0",
    "19.216.8.0",
    "192.1.6.80",
    "192.1.68.0",
    "192.16.8.0",
    "192.168.0.0"
]

Input: "2542540123"
Output: [
    "254.25.40.123",
    "254.254.0.123"
]

Rules:
1. Each part must be valid:
   - Between 0 and 255
   - No leading zeros unless it's just 0
2. Use all digits from the input string
3. Maintain the order of digits
4. Return empty array if no valid IP addresses possible

Parameters:
- string: A string of digits (no dots)

Return:
- Array of all possible valid IP addresses that can be formed from the input
*/

function isValidPart(string) {
    if (parseInt(string) > 255) return false;
    if (String(parseInt(string)) !== string) return false;
    return true;
}

function validIPAddresses(string) {
    const ipAddressesFound = [];
    const parts = ["", "", "", ""];
    for (let p1 = 0; p1 < 3; p1++) {
        for (let p2 = 0; p2 < 3; p2++) {
            for (let p3 = 0; p3 < 3; p3++) {
                if (p1 + p2 + p3 + 3 >= string.length) continue;
                parts[0] = string.slice(0, p1 + 1);
                parts[1] = string.slice(p1 + 1, p1 + p2 + 2);
                parts[2] = string.slice(p1 + p2 + 2, p1 + p2 + p3 + 3);
                parts[3] = string.slice(p1 + p2 + p3 + 3);
                if (isValidPart(parts[0]) && isValidPart(parts[1]) && isValidPart(parts[2]) && isValidPart(parts[3])) {
                    ipAddressesFound.push(parts.join("."));
                }
            }
        }
    }
    return ipAddressesFound;
}

module.exports = validIPAddresses;
