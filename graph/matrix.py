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
        edge = int(lineValues[2])

        self.valueMatrix[node1][node2] = edge
        self.valueMatrix[node2][node1] = edge

    if (not self.file.closed):
        self.file.close()


def squaredMatrix(self):
    return (self.valueMatrix) @ (self.valueMatrix)
