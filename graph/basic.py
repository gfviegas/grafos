def order(self):
    """
    Calcula e retorna a ordem do grafo.

    Args:
        None

    Returns:
        int: ordem (quantidade de vértices) do grafo

    Raises:
        None
    """

    return len(self.valueMatrix)


def neighbors(self, node):
    """
    Busca os vizinhos de um vértice

    Itera a matriz de valores buscando quais vértices estão conectados a um
    vértice fornecido, retornando a lista destes vizinhos.

    Args:
        node (int): índice de um vértice que terá seus vizinhos buscados

    Returns:
        list: lista de vértices vizinhos ao vértice fornecido

    Raises:
        None
    """

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


def isEulerian(self):
    """
    Verifica se o grafo é Euleriano.

    Verifica se o grafo é conexo. Se sim, verifica se o grau de cada vértice
    do grafo é par (Teorema de Euler). Em caso afirmativo para as duas afirmações,
    conclui-se que o grafo é Euleriano.

    Args:
        None

    Returns:
        Boolean: True se o grafo for Euleriano; False em caso contrário

    Raises:
        None
    """

    if not self.isConnected(): return False

    for v in range(self.nodesAmount):
        if self.degree(v) % 2 != 0: return False

    return True

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
