function findThreeLargestNumbers(array) {
    const retval = [Number.NEGATIVE_INFINITY, Number.NEGATIVE_INFINITY, Number.NEGATIVE_INFINITY];
    for (const val of array) {
        if (val > retval[2]) {
            retval[0] = retval[1];
            retval[1] = retval[2];
            retval[2] = val;
        } else if (val > retval[1]) {
            retval[0] = retval[1];
            retval[1] = val;
        } else if (val > retval[0]) {
            retval[0] = val;
        }
    }
    return retval;
}

module.exports = findThreeLargestNumbers;
