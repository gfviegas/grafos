class Graph(object):
    """Graph Parent class """
    def __init__(self, filePath):
        super(Graph, self).__init__()
        self.filePath = filePath
        self.generateValueMatrix()

    def openFile(self):
        self.file = open(self.filePath, 'r')

    def readNodesAmount(self):
        self.nodesAmount = int(self.file.readline())

    def generateValueMatrix(self):
        self.openFile()
        self.readNodesAmount()

        # Inicializa a matriz com 0s
        self.valueMatrix = [[0 for x in range(self.nodesAmount)]
                            for y in range(self.nodesAmount)]

        for line in self.file:
            lineValues = line.split(' ')
            node1 = int(lineValues[0]) - 1
            node2 = int(lineValues[1]) - 1
            edge = int(lineValues[2])

            self.valueMatrix[node1][node2] = edge
            self.valueMatrix[node2][node1] = edge

        if (not self.file.closed):
            self.file.close()

    def printValueMatrix(self):
        print(self.valueMatrix)
