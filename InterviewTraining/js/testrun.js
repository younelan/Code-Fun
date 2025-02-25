const { loadTests } = require('./AlgoHelper/testing');
const path = require('path');

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

function getColorStr(line, color = "OKCYAN") {
    return (TermColors[color] || TermColors["FAIL"]) + line + TermColors["ENDC"];
}

if (process.argv.length < 3) {
    console.log("Usage: node genericRunner.js <moduleName>");
    process.exit(1);
}

let moduleName = process.argv[2];
if (!moduleName) {
    console.log("Usage: node testrun.js <moduleName>");
    process.exit(1);
}

// Remove .js extension if present.
if (moduleName.endsWith('.js')) {
    moduleName = moduleName.slice(0, -3);
}

let solution;
try {
    solution = require(path.join(__dirname, `${moduleName}.js`));
} catch (err) {
    console.error(`Error loading solution for module "${moduleName}":`, err);
    process.exit(1);
}

// Load tests - might return empty array if no test file exists
const tests = loadTests(moduleName);

// Early exit with message if no tests found
if (!tests || tests.length === 0) {
    console.log(getColorStr(`No tests found for module "${moduleName}"`, "WARNING"));
    process.exit(0);
}

console.log(getColorStr(`---- Test ${moduleName} ----`, "HEADER"));

let passedCount = 0;
let failedCount = 0;

tests.forEach((test, idx) => {
    let result;
    const expected = test.expect !== undefined ? test.expect : test.expected;
    const functionName = test.functionName || test.method;

    // Verify the exact function being tested exists
    if (typeof solution === 'function' && solution.name !== functionName) {
        console.error(getColorStr(`Function name mismatch: expected "${functionName}" but found "${solution.name}"`, "FAIL"));
        process.exit(1);
    }

    if (typeof solution !== 'function' && typeof solution[functionName] !== 'function') {
        console.error(getColorStr(`Function "${functionName}" not found in module "${moduleName}"`, "FAIL"));
        process.exit(1);
    }

    if (test.testType === "graph") {
        // Graph tests require building a graph using a class.
        const { loadGraph } = require('./AlgoHelper/graphs');
        const { graph } = test;
        if (solution.name !== test.className) {
            console.error(`Expected class ${test.className} but got ${solution.name}`);
            process.exit(1);
        }
        const { startNode } = loadGraph(graph.nodes, graph.startNode, solution);
        result = startNode[test.method]([]);
    } 
    else if (test.testType === "list") {
        // List tests require building a linked list.
        const { loadList } = require('./AlgoHelper/linkedlist');
        const { head } = loadList(test.nodes, test.headId);
        result = solution(head);
    } 
    else if (test.testType === "tree") {
        // Tree tests require constructing a tree.
        const { buildTree } = require('./AlgoHelper/tree');
        const treeData = test.tree;

        if (test.className === "BST") {
            // Handle BST class specifically
            // Create a new BST instance with the root value
            const rootNode = treeData.nodes.find(n => n.id === treeData.rootId);
            const bst = new solution(rootNode.value);
            
            // Build the tree by inserting all other nodes
            treeData.nodes.forEach(node => {
                if (node.id !== treeData.rootId) {
                    bst.insert(node.value);
                }
            });

            // Depending on the test method, either return the BST or call its method
            if (test.method === "insert") {
                result = bst;
            } else if (test.method === "remove") {
                result = bst.remove(test.value);
            } else {
                result = bst[test.method]();
            }
        } else {
            // Handle other tree types
            const { root } = buildTree(treeData.nodes, treeData.rootId);
            result = typeof solution === "function" ? solution(root) : solution[test.functionName](root, []);
        }
    } 
    else if (test.testType === "function") {
        const input = test.input;
        if (typeof solution === "function") {
            result = Array.isArray(input) ? solution(...input) : solution(input);
        } else if (typeof solution[functionName] === "function") {
            result = Array.isArray(input) ? solution[functionName](...input) : solution[functionName](input);
        }
    } 
    else {
        console.error(`Unrecognized testType: ${test.testType}`);
        process.exit(1);
    }

    // Update comparison to handle edge cases like 0
    const passed = equals(result, expected);
    if (passed) {
        passedCount++;
        console.log(getColorStr(`Test ${idx + 1}: Passed`, "OKGREEN"));
    } else {
        failedCount++;
        console.log(getColorStr(`Test ${idx + 1}: Failed`, "FAIL"));
    }
    if (test.functionName || test.method) {
        console.log(`  Test Name: ${test.functionName || test.method}`);
    }
    // Update result display to handle all types properly
    console.log(`  Returned: ${formatValue(result)}`);
    console.log(`  Expected: ${formatValue(expected)}\n`);
});

const totalTests = passedCount + failedCount;
console.log(getColorStr(`Total Tests: ${totalTests}`, "HEADER"));
console.log(getColorStr(`Passed: ${passedCount}`, "OKGREEN"));
console.log(getColorStr(`Failed: ${failedCount}`, "FAIL"));
console.log(getColorStr(`Success Ratio: ${(passedCount / totalTests * 100).toFixed(2)}%`, "OKCYAN"));
console.log();

// Add these helper functions at the end of the file
function equals(a, b) {
    return JSON.stringify(a) === JSON.stringify(b);
}

function formatValue(value) {
    if (value === undefined) return 'undefined';
    if (value === null) return 'null';
    return JSON.stringify(value);
}
