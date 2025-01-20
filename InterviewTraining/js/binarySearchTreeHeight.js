function binarySearchTreeHeight(root) {
    if (!root) return 0;
    return 1 + Math.max(binarySearchTreeHeight(root.left), binarySearchTreeHeight(root.right));
}

module.exports = binarySearchTreeHeight;
