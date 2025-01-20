function findFirstWrong(array, outlier) {
    let idx = 0;
    while (outlier >= array[idx]) {
        idx++;
    }
    
    const dupeTest = array[idx];
    if (idx < array.length - 1 && array[idx + 1] === dupeTest) {
        while (idx < array.length - 1 && array[idx] === dupeTest) {
            idx++;
        }
    }
    
    return idx;
}

function subarraySort(array) {
    if (array.length < 2) return [-1, -1];
    if (array.length === 2 && array[0] > array[1]) return [0, 1];
    
    let isSorted = true;
    let firstWrong = null;
    let lastWrong = null;
    let minWrongVal, maxWrongVal;
    
    for (let idx = 0; idx < array.length - 1; idx++) {
        const currentVal = array[idx];
        const nextIdx = idx + 1;
        const nextVal = array[nextIdx];
        
        if (isSorted) {
            if (currentVal > nextVal) {
                firstWrong = findFirstWrong(array, nextVal);
                lastWrong = nextIdx;
                minWrongVal = nextVal;
                maxWrongVal = nextVal;
                isSorted = false;
            }
        } else {
            if (nextVal < currentVal) {
                lastWrong = nextIdx;
                
                const tmpMax = Math.max(...array.slice(firstWrong, nextIdx));
                if (tmpMax > maxWrongVal) {
                    maxWrongVal = tmpMax;
                }
                
                if (nextVal > maxWrongVal) {
                    maxWrongVal = nextVal;
                    lastWrong = nextIdx;
                }
            }
            
            if (nextVal < minWrongVal) {
                firstWrong = findFirstWrong(array, minWrongVal);
                minWrongVal = nextVal;
                lastWrong = nextIdx;
            }
        }
    }
    
    return isSorted ? [-1, -1] : [firstWrong, lastWrong];
}

module.exports = subarraySort;
