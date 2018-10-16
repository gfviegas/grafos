def order(self):
    return len(self.valueMatrix)


def neighbors(self, node):
    neighbors = []
    for node, edge in enumerate(self.valueMatrix[node]):
        if (edge != 0):
            neighbors.append(int(node))
    return neighbors

    # return list(filter(lambda k, v: v != 0, self.valueMatrix[node]))


def degree(self, node):
    return sum(1 for v in self.valueMatrix[node] if v != 0)


def edgesAmount(self):
    totalDegrees = sum(self.degree(v) for v in range(0, self.nodesAmount))
    return int(totalDegrees / 2)  # Utilizando handshaking lemma


def size(self):
    return self.edgesAmount() + self.nodesAmount


def isConnected(self):
    info = self.depthFirstSearch()
    return (len(info["connectedComponents"]) == 1)


def isArticulation(self, node):
    connectedComponents = len((self.depthFirstSearch())["connectedComponents"])
    filteredGraph = self.filteredNode(node)
    filteredGraphConnectedComponents = len((filteredGraph.depthFirstSearch())["connectedComponents"])
    return (filteredGraphConnectedComponents > connectedComponents)


def isBridge(self, edge):
    connectedComponents = len((self.depthFirstSearch())["connectedComponents"])
    filteredGraph = self.filteredEdge(edge)
    filteredGraphConnectedComponents = len((filteredGraph.depthFirstSearch())["connectedComponents"])
    return (filteredGraphConnectedComponents > connectedComponents)
