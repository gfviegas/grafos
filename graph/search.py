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


def isBipartite(self, node=0):
    # Sem cor = -1, Primeira cor = 1, Segunda cor = 0
    colorArray = [-1] * self.order()

    # O primeiro vértice recebe a primeira cor
    colorArray[node] = 1

    queue = []
    queue.append(node)

    # Enquanto tiver vértices na fila...
    while queue:
        u = queue.pop()

        if self.valueMatrix[u][u] == 1:
            return False

        for v in self.neighbors(u):
            # Se o vértice vizinho não tiver colorido, colore-o
            if colorArray[v] == -1:
                colorArray[v] = 1 - colorArray[u]
                queue.append(v)  # e o adicione na fila
            elif colorArray[v] == colorArray[u]:
                return False
    return True
