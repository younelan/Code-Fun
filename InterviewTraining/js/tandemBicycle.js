function tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest) {
    let totalSpeed = 0;
    const sortedRed = [...redShirtSpeeds].sort((a, b) => a - b);
    const sortedBlue = [...blueShirtSpeeds].sort((a, b) => a - b);

    for (let i = 0; i < sortedRed.length; i++) {
        let redSpeed, blueSpeed;
        
        if (fastest) {
            if (sortedRed[sortedRed.length - 1] > sortedBlue[sortedBlue.length - 1]) {
                redSpeed = sortedRed.pop();
                blueSpeed = sortedBlue.shift();
            } else {
                redSpeed = sortedRed.shift();
                blueSpeed = sortedBlue.pop();
            }
        } else {
            redSpeed = sortedRed.shift();
            blueSpeed = sortedBlue.shift();
        }
        
        totalSpeed += Math.max(redSpeed, blueSpeed);
    }

    return totalSpeed;
}

module.exports = tandemBicycle;
