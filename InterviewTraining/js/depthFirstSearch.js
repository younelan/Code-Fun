class Node {
    constructor(name) {
        this.name = name;
        this.children = [];
    }
    addChild(childNode) {
        this.children.push(childNode);
        return this;
    }
    depthFirstSearch(array) {
        array.push(this.name);
        this.children.forEach(child => child.depthFirstSearch(array));
        return array;
    }
}

module.exports = Node;
