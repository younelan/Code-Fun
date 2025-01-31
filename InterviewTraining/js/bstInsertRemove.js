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
        return this;
    }

    contains(value) {
        if (value === this.value) {
            return true;
        } else if (value < this.value) {
            return this.left ? this.left.contains(value) : false;
        } else {
            return this.right ? this.right.contains(value) : false;
        }
    }

    remove(value, parent = null) {
        if (value < this.value) {
            if (this.left) {
                this.left.remove(value, this);
            }
        } else if (value > this.value) {
            if (this.right) {
                this.right.remove(value, this);
            }
        } else {
            if (this.left && this.right) {
                this.value = this.right.getMinValue();
                this.right.remove(this.value, this);
            } else if (parent === null) {
                if (this.left) {
                    this.value = this.left.value;
                    this.right = this.left.right;
                    this.left = this.left.left;
                } else if (this.right) {
                    this.value = this.right.value;
                    this.left = this.right.left;
                    this.right = this.right.right;
                } else {
                    // Do nothing, this is a single-node tree; do not remove the root node.
                }
            } else if (parent.left === this) {
                parent.left = this.left ? this.left : this.right;
            } else if (parent.right === this) {
                parent.right = this.left ? this.left : this.right;
            }
        }
        return this;
    }

    getMinValue() {
        if (this.left === null) {
            return this.value;
        } else {
            return this.left.getMinValue();
        }
    }
}

module.exports = BST;
