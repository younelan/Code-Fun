const fs = require('fs');
const path = require('path');

function loadTests(moduleName) {
    const testFile = path.join(__dirname, '..', '..', 'tests', `${moduleName}.json`);
    try {
        const contents = fs.readFileSync(testFile, 'utf8');
        return JSON.parse(contents);
    } catch (error) {
        if (error.code === 'ENOENT') {
            console.log(`No test file found for module "${moduleName}"`);
            return [];
        }
        // Re-throw any other errors
        throw error;
    }
}

module.exports = { loadTests };
