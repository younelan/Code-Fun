function longestPeak(array) {
    let maxPeak = 0;
    if (array.length < 3) return 0;

    let idx = 1;
    while (idx < array.length - 1) {
        const isPeak = array[idx - 1] < array[idx] && array[idx + 1] < array[idx];
        if (isPeak) {
            let start = idx;
            while (start > 0 && array[start - 1] < array[start]) {
                start--;
            }
            let end = idx;
            while (end < array.length - 1 && array[end + 1] < array[end]) {
                end++;
            }
            maxPeak = Math.max(maxPeak, end - start + 1);
            idx = end;
        }
        idx++;
    }
    return maxPeak;
}

module.exports = longestPeak;
