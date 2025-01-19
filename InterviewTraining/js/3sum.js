function threeNumberSum(array, targetSum) {
    const arrSorted = array.slice().sort((a, b) => a - b);
    const retval = [];
    for (let i = 0; i < arrSorted.length - 2; i++) {
        for (let j = i + 1; j < arrSorted.length - 1; j++) {
            for (let k = j + 1; k < arrSorted.length; k++) {
                if (arrSorted[i] + arrSorted[j] + arrSorted[k] === targetSum) {
                    retval.push([arrSorted[i], arrSorted[j], arrSorted[k]]);
                }
            }
        }
    }
    return retval;
}

module.exports = threeNumberSum;
