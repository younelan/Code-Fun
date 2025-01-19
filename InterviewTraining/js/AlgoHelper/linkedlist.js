const { getColorStr, printColor } = require('./console');

class LinkedList {
    constructor(value, name = null) {
        this.value = value;
        this.next = null;
        this.id_str = name ? name : String(value);
    }
    toString() {
        const nextStr = this.next ? this.next.idStr : "None";
        return `<<LinkedList id ${this.idStr} value ${this.value} next ${nextStr}>>`;
    }
}

function getListStr(head) {
    let ptr = head, vals = [];
    while (ptr) {
        vals.push(String(ptr.value));
        ptr = ptr.next;
    }
    return vals.join(" -> ");
}

function loadList(nodes, headStr) {
    const items = {};
    nodes.forEach(item => {
        items[item.id] = new LinkedList(item.value, item.id);
    });
    nodes.forEach(item => {
        if (item.next) {
            items[item.id].next = items[item.next];
        }
    });
    return items[headStr];
}

function printList(head, color = null) {
    printColor(getListStr(head), color);
}

module.exports = { LinkedList, getListStr, loadList, printList };
