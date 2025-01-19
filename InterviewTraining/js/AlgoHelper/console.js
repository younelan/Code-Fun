const TermColors = {
    "HEADER": '\x1B[95m',
    "OKBLUE": '\x1B[94m',
    "OKCYAN": '\x1B[96m',
    "OKGREEN": '\x1B[92m',
    "WARNING": '\x1B[93m',
    "FAIL": '\x1B[91m',
    "ENDC": '\x1B[0m',
    "BOLD": '\x1B[1m',
    "UNDERLINE": '\x1B[4m'
};

const defaultColor = "OKCYAN";

function arrayToStr(array) {
    const retlist = array.map(val => {
        if (Array.isArray(val)) return arrayToStr(val);
        return typeof val === "string" ? val : String(val);
    });
    return "[ " + retlist.join(", ") + " ]";
}

function getColorStr(line, color = defaultColor) {
    if (Array.isArray(line)) line = arrayToStr(line);
    else if (typeof line !== "string") line = JSON.stringify(line);
    return (TermColors[color] || TermColors["FAIL"]) + line + TermColors["ENDC"];
}

function printColor(line, color = defaultColor) {
    console.log(getColorStr(line, color));
}

function scriptHeader(line) {
    const offset = Math.floor(line.length / 2);
    printColor("_".repeat(60), "WARNING");
    printColor(" ".repeat(30 - offset) + line, "WARNING");
    printColor("_".repeat(60), "WARNING");
}

function testHeader(line) {
    const offset = Math.floor(line.length / 2);
    line = `\n${"*".repeat(29 - offset)} ${line} ${"*".repeat(29 - offset)}`;
    printColor(line, "WARNING");
}

function sectionHeader(line) {
    const offset = Math.floor(line.length / 2);
    line = `\n${"-".repeat(29 - offset)} ${line} ${"-".repeat(29 - offset)}`;
    printColor(line, "WARNING");
}

module.exports = {
    TermColors,
    getColorStr,
    printColor,
    scriptHeader,
    testHeader,
    sectionHeader
};
