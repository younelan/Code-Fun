function inOrderTraverse(tree, array) {
    if (!tree) return array;
    inOrderTraverse(tree.left, array);
    array.push(tree.value);
    inOrderTraverse(tree.right, array);
    return array;
}

function preOrderTraverse(tree, array) {
    if (!tree) return array;
    array.push(tree.value);
    preOrderTraverse(tree.left, array);
    preOrderTraverse(tree.right, array);
    return array;
}

function postOrderTraverse(tree, array) {
    if (!tree) return array;
    postOrderTraverse(tree.left, array);
    postOrderTraverse(tree.right, array);
    array.push(tree.value);
    return array;
}

module.exports = { inOrderTraverse, preOrderTraverse, postOrderTraverse };
