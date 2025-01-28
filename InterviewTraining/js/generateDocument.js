function generateDocument(characters, document) {
    for (const char of document) {
        const pos = characters.indexOf(char);
        if (pos === -1) {
            return false;
        } else {
            characters = characters.slice(0, pos) + characters.slice(pos + 1);
        }
    }
    return true;
}

module.exports = generateDocument;
