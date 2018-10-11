def order(self):
    return (self.nodesAmount)


def neighbors(self, node):
    return list(filter(lambda v: v != 0, self.valueMatrix[node]))


def degree(self, node):
    return sum(1 for v in self.valueMatrix[node] if v != 0)


def edgesAmount(self):
    totalDegrees = sum(self.degree(v) for v in range(0, self.nodesAmount))
    return int(totalDegrees / 2)  # Utilizando handshaking lemma


def size(self):
    return self.edgesAmount() + self.nodesAmount


def isConnected(self, matrix=None):
    if matrix is None:
        matrix = self.valueMatrix

    for line in range(0, self.nodesAmount):
        degree = sum(v for v in matrix[line] if v != 0)
        if (degree <= 0):
            return False
    return True


def isArticulation(self, node):
    filteredMatrix = self.filteredNode(node)
    return not(self.isConnected(filteredMatrix))
