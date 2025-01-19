function mergeOverlappingIntervals(intervals) {
    const result = [];
    while (intervals.length) {
        let range1 = intervals.shift();
        let [minval, maxval] = range1;
        const mergedRanges = [];
        for (let i = 0; i < intervals.length; i++) {
            const range2 = intervals[i];
            if (
                (range1[0] >= range2[0] && range1[0] <= range2[1]) ||
                (range1[1] <= range2[0] && range1[1] >= range2[1]) ||
                (range2[0] >= range1[0] && range2[0] <= range1[1]) ||
                (range2[1] <= range1[0] && range2[1] >= range1[1])
            ) {
                mergedRanges.push(i);
                range1 = [
                    Math.min(range1[0], range2[0]),
                    Math.max(range1[1], range2[1])
                ];
            }
        }
        if (mergedRanges.length) {
            for (let i = mergedRanges.length - 1; i >= 0; i--) {
                intervals.splice(mergedRanges[i], 1);
            }
            intervals.push(range1);
        } else {
            result.push(range1);
        }
    }
    return result;
}

module.exports = mergeOverlappingIntervals;
