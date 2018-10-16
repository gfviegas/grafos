import numpy
from .edges import translateEdgeNotation


def generateValueMatrix(self):
    self.openFile()
    self.readNodesAmount()

    if (not self.nodesAmount or self.nodesAmount <= 0):
        raise Exception('nodesAmountNotDefined')

    # Inicializa a matriz com 0s
    self.valueMatrix = numpy.zeros(
        shape=(self.nodesAmount, self.nodesAmount),
        dtype=float
    )

    for line in self.file:
        lineValues = line.split(' ')
        node1 = int(lineValues[0]) - 1
        node2 = int(lineValues[1]) - 1
        edge = float(lineValues[2])

        self.valueMatrix[node1][node2] = edge
        self.valueMatrix[node2][node1] = edge

    if (not self.file.closed):
        self.file.close()


def squaredMatrix(self):
    return (self.valueMatrix) @ (self.valueMatrix)


# Retorna uma cópia do grafo sem uma arestas
def filteredEdge(self, edge):
    from graph import Graph
    filteredMatrix = numpy.copy(self.valueMatrix)
    edgeNodes = list(map(lambda e: e - 1, translateEdgeNotation(edge)))

    filteredMatrix[edgeNodes[0]][edgeNodes[1]] = 0
    filteredMatrix[edgeNodes[1]][edgeNodes[0]] = 0

    graph = Graph()
    graph.valueMatrix = filteredMatrix
    graph.nodesAmount = graph.order()

    return graph


# Retorna uma cópia do grafo sem um vértice e suas arestas
def filteredNode(self, node):
    from graph import Graph
    filteredMatrix = numpy.copy(self.valueMatrix)
    filteredMatrix = numpy.delete(filteredMatrix, node, 0)
    filteredMatrix = numpy.delete(filteredMatrix, node, 1)

    graph = Graph()
    graph.valueMatrix = filteredMatrix
    graph.nodesAmount = graph.order()

    return graph
