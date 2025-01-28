function largestRange(array) {
    const arr = array.slice().sort((a, b) => a - b);
    if (arr.length === 1) return [arr[0], arr[0]];
    if (arr.length === 2) return arr;

    let first = arr.shift();
    let prev = first;
    let last = first;
    let minval = first;
    let maxval = first;
    let count = 0;

    while (arr.length) {
        const cur = arr.shift();
        if (cur === prev) continue;
        if (prev + 1 === cur) {
            count++;
            last = cur;
            if (last - first > maxval - minval) {
                minval = first;
                maxval = last;
            }
        } else {
            first = cur;
            count = 1;
        }
        prev = cur;
    }
    return [minval, maxval];
}

module.exports = largestRange;
