class BinaryTree {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

function branchSums(root, sums = [], curTotal = 0) {
    if (!root) return sums;

    curTotal += root.value;
    if (!root.left && !root.right) {
        sums.push(curTotal);
    }

    if (root.left) {
        branchSums(root.left, sums, curTotal);
    }
    if (root.right) {
        branchSums(root.right, sums, curTotal);
    }

    return sums;
}

module.exports = { BinaryTree, branchSums };
