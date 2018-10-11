import numpy


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


# Retorna uma cópia da matriz sem um vértice e suas arestas
def filteredNode(self, node):
    filteredMatrix = numpy.copy(self.valueMatrix)
    filteredMatrix[node] = numpy.zeros(self.nodesAmount)
    for line in range(0, self.nodesAmount):
        filteredMatrix[line][node - 1] = 0

    return filteredMatrix
