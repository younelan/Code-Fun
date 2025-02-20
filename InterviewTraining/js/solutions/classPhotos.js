/*
Class Photos

It's photo day at school! You are a teacher trying to arrange students in two rows for a class photo.

Problem:
- You have two arrays representing heights of students
- One array for students wearing red shirts
- One array for students wearing blue shirts
- Each row must have the same number of students
- All students in front row must be strictly shorter than students behind them
- All students wearing the same color shirt must be in the same row

Your task:
Write a function that determines whether you can arrange the students in two rows following these rules.

Parameters:
redShirtHeights = [5, 8, 1, 3, 4]   // Heights of students wearing red
blueShirtHeights = [6, 9, 2, 4, 5]  // Heights of students wearing blue

Rules:
1. One row must be all RED shirts, the other all BLUE shirts
2. The back row students must each be STRICTLY TALLER than the student directly in front of them
3. Each row must contain the same number of students
4. You cannot mix shirt colors in the same row

Example 1:
redShirtHeights = [5, 8, 1, 3, 4]
blueShirtHeights = [6, 9, 2, 4, 5]
Returns: true
Because you can arrange them like this:
Back row:    [9, 8, 4, 5, 6]  (BLUE)
Front row:   [4, 3, 1, 2, 5]  (RED)

Example 2:
redShirtHeights = [6, 9, 2, 4, 5]
blueShirtHeights = [5, 8, 1, 3, 4]
Returns: false
Because some students in front would be taller than those behind

Return:
- true if you can arrange the photo following all rules
- false if it's impossible to arrange the photo following all rules
*/

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
