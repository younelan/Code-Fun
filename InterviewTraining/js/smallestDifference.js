function smallestDifference(arrayOne, arrayTwo) {
    let minDiff = Infinity;
    let result = [];
    for (let i = 0; i < arrayOne.length; i++) {
        for (let j = 0; j < arrayTwo.length; j++) {
            const diff = Math.abs(arrayOne[i] - arrayTwo[j]);
            if (diff < minDiff) {
                minDiff = diff;
                result = [arrayOne[i], arrayTwo[j]];
            }
        }
    }
    return result;
}

module.exports = smallestDifference;
