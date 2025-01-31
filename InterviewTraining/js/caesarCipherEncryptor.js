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
