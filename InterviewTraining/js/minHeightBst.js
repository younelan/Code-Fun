class BST {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }

    insert(value) {
        if (value < this.value) {
            if (this.left === null) {
                this.left = new BST(value);
            } else {
                this.left.insert(value);
            }
        } else {
            if (this.right === null) {
                this.right = new BST(value);
            } else {
                this.right.insert(value);
            }
        }
    }
}

function minHeightBst(input) {
    // Input from genericRunner comes as first element of array
    const array = Array.isArray(input) ? input : [input];
    
    if (!array || array.length === 0) return null;
    
    function buildBST(start, end) {
        if (start > end) return null;
        
        const mid = Math.floor((start + end) / 2);
        const node = new BST(array[mid]);
        
        node.left = buildBST(start, mid - 1);
        node.right = buildBST(mid + 1, end);
        
        return node;
    }
    
    const sortedArray = array.slice().sort((a, b) => a - b);
    return buildBST(0, sortedArray.length - 1);
}

module.exports = minHeightBst;
