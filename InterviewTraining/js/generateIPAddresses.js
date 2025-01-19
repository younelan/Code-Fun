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
