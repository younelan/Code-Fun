const { getColorStr } = require('./console');

class BinarySearchTree {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

function printNode(root) {
    const leftVal = root.left ? JSON.stringify(root.left.value) : "None";
    const rightVal = root.right ? JSON.stringify(root.right.value) : "None";
    const idVal = JSON.stringify(root.value);
    console.log(`  << ${getColorStr("Node:", "FAIL")} ${getColorStr(idVal, "BOLD")}  ${getColorStr("Left:", "FAIL")} ${getColorStr(leftVal, "BOLD")}  ${getColorStr("Right:", "FAIL")} ${getColorStr(rightVal, "BOLD")} >> `);
}

function outputTree(root, depth = 0, isLeft = 0) {
    let pos;
    if (isLeft === 0) pos = "Root";
    else if (isLeft === -1) pos = "Left";
    else if (isLeft === 1) pos = "Right";
    const rootColor = getColorStr(root.value, "OKCYAN");
    const posColor = getColorStr(pos, "OKGREEN");
    console.log(`${"    ".repeat(depth + 1)} ${rootColor} (${posColor})`);
    const newDepth = depth + 1;
    if (root.left) outputTree(root.left, newDepth, -1);
    if (root.right) outputTree(root.right, newDepth, 1);
}

function buildTree(tree, rootId) {
    const nodes = {};
    tree.forEach(item => {
        nodes[item.id] = new BinarySearchTree(item.value);
    });
    tree.forEach(item => {
        if (item.left) {
            nodes[item.id].left = nodes[item.left];
        }
        if (item.right) {
            nodes[item.id].right = nodes[item.right];
        }
    });
    return { root: nodes[rootId], nodes };
}

module.exports = { BinarySearchTree, printNode, outputTree, buildTree };
