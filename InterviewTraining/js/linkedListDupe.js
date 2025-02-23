/*
Remove Duplicates From Linked List

You're given the head of a Sorted Singly Linked List. Write a function that returns
the modified list after removing all duplicate values. The linked list should be
modified in place (don't create a new list).

Example of creating and using the list:

// Create nodes
const node1 = new LinkedList(1);
const node2 = new LinkedList(1);
const node3 = new LinkedList(1);
const node4 = new LinkedList(2);
const node5 = new LinkedList(3);
const node6 = new LinkedList(3);

// Connect nodes
node1.next = node2;
node2.next = node3;
node3.next = node4;
node4.next = node5;
node5.next = node6;

// Before: 1 -> 1 -> 1 -> 2 -> 3 -> 3
const result = removeDuplicatesFromLinkedList(node1);
// After: 1 -> 2 -> 3

Another example:
const list = new LinkedList(1);
list.next = new LinkedList(1);
list.next.next = new LinkedList(1);
list.next.next.next = new LinkedList(4);
list.next.next.next.next = new LinkedList(4);
list.next.next.next.next.next = new LinkedList(5);
removeDuplicatesFromLinkedList(list);
// Returns: 1 -> 4 -> 5

Important Notes:
- The linked list will always be sorted (numbers in ascending order)
- You should remove all duplicates, so each value appears only once
- Modify the list in place - don't create a new list
- Return the head of the modified linked list

Example:
Input:  1 -> 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 4 -> 5
Output: 1 -> 2 -> 3 -> 4 -> 5

Input:  1 -> 1 -> 1 -> 1 -> 1 -> 4 -> 4 -> 5 -> 6 -> 6
Output: 1 -> 4 -> 5 -> 6

Each LinkedList node has:
- value: The node's value (number)
- next: Points to next node or null if it's the tail

Parameters:
- linkedList: The head node of a sorted linked list

Return:
- The head of the modified linked list with duplicates removed

Hints:
- Since the list is sorted, duplicates will always be adjacent
- You can traverse the list once to solve this
- Think about how to "skip over" duplicate values
*/

class LinkedList {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

function removeDuplicatesFromLinkedList(linkedList) {
    // Write your code here
    // Remember to handle empty list and single node cases
    return linkedList;
}

module.exports = removeDuplicatesFromLinkedList;
