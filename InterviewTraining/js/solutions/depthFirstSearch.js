/*
Depth First Search

You're given a Node class that has a name and an array of optional children nodes.
Implement the depthFirstSearch method on the Node class, which takes in an empty array and
returns an array of all the nodes' names in Depth-first Search (DFS) order.

What is Depth-first Search?
- Start at the root node
- Traverse as far down a branch as possible before backtracking
- Visit children from left to right
- Add each node's name to the array as you visit it

Example tree:
         A
       / | \
      B  C  D
     / \    / \
    E   F  G   H
       / \  \
      I   J  K

Sample input:
const node = new Node("A");
node.addChild(new Node("B"));
node.addChild(new Node("C"));
node.addChild(new Node("D"));
node.children[0].addChild(new Node("E"));
node.children[0].addChild(new Node("F"));
node.children[2].addChild(new Node("G"));
node.children[2].addChild(new Node("H"));

Sample output:
["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]

Note:
- The Node class is already created with name and children properties
- addChild method is implemented for you
- You only need to implement the depthFirstSearch method
- The input array will be empty when first called
*/

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
