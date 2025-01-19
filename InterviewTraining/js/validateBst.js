function validateBst(tree, minVal = -Infinity, maxVal = Infinity) {
    if (!tree) return true;
    if (tree.value < minVal || tree.value >= maxVal) return false;

    const leftValid = validateBst(tree.left, minVal, tree.value);
    const rightValid = validateBst(tree.right, tree.value, maxVal);

    return leftValid && rightValid;
}

module.exports = validateBst;
