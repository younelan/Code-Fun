function classPhotos(redShirtHeights, blueShirtHeights) {
    const sortedRed = redShirtHeights.slice().sort((a, b) => a - b);
    const sortedBlue = blueShirtHeights.slice().sort((a, b) => a - b);
    let blueFront = true;
    let redFront = true;

    for (let i = 0; i < sortedRed.length; i++) {
        if (sortedRed[i] <= sortedBlue[i]) {
            redFront = false;
        }
        if (sortedBlue[i] <= sortedRed[i]) {
            blueFront = false;
        }
    }

    return blueFront || redFront;
}

module.exports = classPhotos;
