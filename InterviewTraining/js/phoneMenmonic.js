const dialpad = {
    1: "1",
    2: "2ABC",
    3: "3DEF",
    4: "4GHI",
    5: "5JKL",
    6: "6MNO",
    7: "7PQRS",
    8: "8TUV",
    9: "9WXYZ"
};

function phoneNumberMnemonics(phoneNumber) {
    const lists = [];
    for (const digit of phoneNumber) {
        lists.push(dialpad[digit]);
    }
    return lists;
}

module.exports = phoneNumberMnemonics;
