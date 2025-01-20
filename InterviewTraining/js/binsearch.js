function binarySearch(array, target) {
    let low_bound = 0, high_bound = array.length;
    let idx = 0;
    while (high_bound - low_bound > 0 && idx < 20) {
        idx++;
        const median = low_bound + Math.floor((high_bound - low_bound) / 2);
        if (array[median] === target) return median;
        if (array[median] > target) {
            high_bound = median;
        } else if (array[median] < target) {
            low_bound = median + 1;
        } else {
            if (median < array.length && array[median + 1] === target) return median + 1;
            return -1;
        }
    }
    return -1;
}

module.exports = binarySearch;
