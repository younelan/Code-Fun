function firstDuplicateValue(array) {
    const counts = {};
    for (const el of array) {
        counts[el] = (counts[el] || 0) + 1;
        if (counts[el] > 1) {
            return el;
        }
    }
    return -1;
}

module.exports = firstDuplicateValue;
