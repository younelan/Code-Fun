const fs = require('fs');
const path = require('path');

function loadTests(moduleName) {
    const testFile = path.join(__dirname, '..', '..', 'tests', `${moduleName}.json`);
    const contents = fs.readFileSync(testFile, 'utf8');
    return JSON.parse(contents);
}

module.exports = { loadTests };
