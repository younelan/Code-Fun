/*
Minimum Waiting Time

You have a list of queries that need to be executed. Each query takes a certain
amount of time to execute, and you can only run one query at a time. Calculate
the minimum total waiting time for all queries to complete.

What is Waiting Time?
- The waiting time for a query is the amount of time it must wait before starting
- Each query must wait for all queries before it to finish
- The total waiting time is the sum of all individual waiting times

Example:
queries = [3, 2, 1, 2, 6]

If executed in this order:
- 3: waits 0  seconds
- 2: waits 3  seconds
- 1: waits 5  seconds
- 2: waits 6  seconds
- 6: waits 8  seconds
Total = 0 + 3 + 5 + 6 + 8 = 22 seconds

But if we reorder to [1, 2, 2, 3, 6]:
- 1: waits 0  seconds
- 2: waits 1  seconds
- 2: waits 3  seconds
- 3: waits 5  seconds
- 6: waits 8  seconds
Total = 0 + 1 + 3 + 5 + 8 = 17 seconds (minimum possible)

Parameters:
- queries: Array of non-negative integers representing query execution times

Return:
- Integer representing the minimum total waiting time

Hints:
- Think about which queries should be executed first
- Consider how each query's execution time affects all queries after it
- The order of execution matters!
*/

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
