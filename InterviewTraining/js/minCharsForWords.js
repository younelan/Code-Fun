function minimumCharactersForWords(words) {
    const retFrequencies = {};
    for (const word of words) {
        const frequencies = {};
        for (const letter of word) {
            frequencies[letter] = (frequencies[letter] || 0) + 1;
            if (frequencies[letter] > (retFrequencies[letter] || 0)) {
                retFrequencies[letter] = frequencies[letter];
            }
        }
    }
    const result = [];
    for (const [letter, count] of Object.entries(retFrequencies)) {
        result.push(...Array(count).fill(letter));
    }
    return result;
}

module.exports = minimumCharactersForWords;
