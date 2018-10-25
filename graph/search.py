from .edges import formatEdgeString


def depthSearch(self, node, visitedNodes, visitedEdges, returnEdges):
    visitedNodes.append(int(node))
    for w in self.neighbors(node):
        w = int(w)

        edge = formatEdgeString(node, w)
        if (edge not in visitedEdges):
            if (abs(node - w) > 1):
                returnEdges.append(edge)
            visitedEdges.append(edge)

        if w not in visitedNodes:
            self.depthSearch(w, visitedNodes, visitedEdges, returnEdges)


def depthFirstSearch(self, node=0):
    info = {"returnEdges": [], "visitedEdges": [], "connectedComponents": []}
    visitedNodes = []
    lastVisitedNodes = []
    notVisitedNodes = range(0, self.nodesAmount)

    while True:
        self.depthSearch(node, visitedNodes, info["visitedEdges"], info["returnEdges"])
        info["connectedComponents"].append(list(filter(lambda v: v not in lastVisitedNodes, visitedNodes)))
        lastVisitedNodes = list(visitedNodes)
        notVisitedNodes = list(filter(lambda v: v not in visitedNodes, range(0, self.nodesAmount)))
        if (len(notVisitedNodes) <= 0):
            break
        node = int(notVisitedNodes[0])
    return info
