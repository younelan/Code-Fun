function minimumWaitingTime(queries) {
    let current = 0;
    let sum = 0;

    if (queries.length < 2) {
        return 0;
    }
    for (const el of queries.sort((a, b) => a - b)) {
        sum += current;
        current += el;
    }

    return sum;
}

module.exports = minimumWaitingTime;
