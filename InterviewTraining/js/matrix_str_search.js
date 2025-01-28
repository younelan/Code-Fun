function matrix_search(M, S) {
    const width = M[0].length;
    const height = M.length;
    for (let x = 0; x < width; x++) {
        for (let y = 0; y < height; y++) {
            if (M[y][x] === S[0]) {
                const [found, direction] = full_word_search(M, x, y, S);
                if (found) {
                    return [true, direction];
                }
            }
        }
    }
    return [false, ""];
}

function full_word_search(M, startX, startY, target) {
    const width = M[0].length;
    const height = M.length;
    const searchParams = [
        [1, 1, "south-east"], [-1, -1, "south-west"], [1, 0, "south"],
        [0, 1, "east"], [0, -1, "west"], [-1, 0, "north"]
    ];

    for (const [dx, dy, direction] of searchParams) {
        let idx = 0;
        let col = startX;
        let row = startY;
        const tLength = target.length;
        while (row >= 0 && col >= 0 && col < width && row < height && M[row][col] === target[idx]) {
            idx++;
            row += dx;
            col += dy;
            if (idx === tLength) {
                return [true, direction];
            }
        }
    }
    return [false, ""];
}

module.exports = matrix_search;
