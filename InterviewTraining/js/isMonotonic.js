function isMonotonic(array) {
    if (array.length < 3) return true;

    let prevElement = array[0];
    let prevDirection = 0;

    for (let i = 1; i < array.length; i++) {
        const curElement = array[i];
        let curDirection = 0;
        if (curElement > prevElement) {
            curDirection = 1;
            if (prevDirection === -1) return false;
        } else if (curElement < prevElement) {
            curDirection = -1;
            if (prevDirection === 1) return false;
        }
        prevElement = curElement;
        if (prevDirection === 0) {
            prevDirection = curDirection;
        }
    }
    return true;
}

module.exports = isMonotonic;
