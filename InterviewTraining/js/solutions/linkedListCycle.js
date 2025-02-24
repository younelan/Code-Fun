/*
Linked List Cycle Detection

Write a function that determines if a linked list contains a cycle.
A cycle occurs when a node's next pointer points to a previous node in the list,
creating a loop.

What is a cycle?
- A cycle exists when you can reach the same node again by following 'next' pointers
- The cycle can occur anywhere in the linked list
- Not all nodes need to be part of the cycle

Examples:

1. List with cycle:
   1 -> 2 -> 3 -> 4 -> 5 -> 3 (points back to 3)
   Returns: true

2. List without cycle:
   1 -> 2 -> 3 -> 4 -> null
   Returns: false

3. Single node cycle:
   1 -> 1 (points to itself)
   Returns: true

4. Empty list:
   null
   Returns: false

Parameters:
- head: The first node of a linked list
  * Each node has properties:
    - value: The node's value
    - next: Reference to next node or null

Return:
- boolean: true if cycle exists, false otherwise

Hints:
- Think about using two pointers moving at different speeds
- What happens when two people run around a track at different speeds?
- Consider memory usage - can you solve it with O(1) space?
*/
function hasCycle(head) {
    let slow = head, fast = head;
    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow === fast) return true;
    }
    return false;
}

module.exports = hasCycle;
