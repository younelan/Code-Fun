function spiralTraverse(array) {
    let minX = 0, minY = 0;
    let maxX = array[0].length - 1, maxY = array.length - 1;
    const result = [];

    while (minX <= maxX && minY <= maxY) {
        // Top row
        for (let col = minX; col <= maxX; col++) {
            result.push(array[minY][col]);
        }

        // Right column
        for (let row = minY + 1; row <= maxY; row++) {
            result.push(array[row][maxX]);
        }

        if (maxY > minY) {
            // Bottom row
            for (let col = maxX - 1; col >= minX; col--) {
                result.push(array[maxY][col]);
            }
        }

        if (maxX > minX) {
            // Left column
            for (let row = maxY - 1; row > minY; row--) {
                result.push(array[row][minX]);
            }
        }

        minX++;
        maxX--;
        minY++;
        maxY--;
    }

    return result;
}

module.exports = spiralTraverse;
