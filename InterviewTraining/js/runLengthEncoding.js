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
