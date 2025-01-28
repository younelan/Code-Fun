class LinkedList {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

function removeDuplicatesFromLinkedList(linkedList) {
    let curPtr = linkedList;
    while (curPtr && curPtr.next) {
        if (curPtr.next.value === curPtr.value) {
            let nextPtr = curPtr.next.next;
            while (nextPtr && nextPtr.value === curPtr.value) {
                nextPtr = nextPtr.next;
            }
            curPtr.next = nextPtr;
        }
        curPtr = curPtr.next;
    }
    return linkedList;
}

module.exports = removeDuplicatesFromLinkedList;
