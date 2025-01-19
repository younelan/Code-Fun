
function loadGraph(nodesData, startNodeId, NodeClass) {
    const nodes = {};
    nodesData.forEach(data => {
        nodes[data.id] = new NodeClass(data.value);
    });
    nodesData.forEach(data => {
        data.children.forEach(childId => {
            nodes[data.id].addChild(nodes[childId]);
        });
    });
    return { startNode: nodes[startNodeId], nodes };
}

module.exports = { loadGraph };