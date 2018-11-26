#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
    Busca os vizinhos de um vértice.

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
    """
    Calcula e retorna o grau de um vértice.

    Percorre a matriz de valores do grafo no índice do nó em questão, incrementando
    1 a cada peso diferente de 0 encontrado.

    Args:
        node (int): índice do nó cujo grau será calculado.

    Returns:
        int: somatório que representa o grau do nó.

    Raises:
        None
    """

    return sum(1 for v in self.valueMatrix[node] if v != 0)


def edgesAmount(self):
    """
    Calcula e retorna o total de arestas presentes no grafo.

    Utiliza o Handshaking Lemma para calcular o total de arestas do grafo.

    Args:
        None

    Returns:
        int: total de arestas presentes no grafo.

    Raises:
        None
    """

    totalDegrees = sum(self.degree(v) for v in range(0, self.nodesAmount))
    return int(totalDegrees / 2)  # Utilizando handshaking lemma


def size(self):
    """
    Calcula e retorna o tamanho do grafo.

    O tamanho do grafo é dado através da soma do total de arestas com o total
    de vértices.

    Args:
        None

    Returns:
        int: valor que representa o tamanho do grafo.

    Raises:
        None
    """

    return self.edgesAmount() + self.nodesAmount


def isConnected(self):
    """
    Verifica a conexidade do grafo.

    Realiza a busca em profundidade no grafo para obter o número de componentes
    conexas.

    Args:
        None

    Returns:
        boolean: True se o número de componentes conexas for 1; False se o número
        for maior.

    Raises:
        None
    """

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
        if self.degree(v) % 2 != 0:
            return False

    return True

def isArticulation(self, node):
    """
    Verifica se um nó é uma articulação.

    Percorre as componentes conexas do grafo, filtrando as componentes conexas
    em detrimento do nó. Se o número de componentes filtradas for maior do que
    o número de componentes originais, então o nó é uma articulação.

    Args:
        node (int): nó a ser verificado como articulação.

    Returns:
        boolean: True se o nó em questão for uma articulação; False caso contrário.

    Raises:
        None
    """

    connectedComponents = len((self.depthFirstSearch())["connectedComponents"])
    filteredGraph = self.filteredNode(node)
    filteredGraphConnectedComponents = len((filteredGraph.depthFirstSearch())["connectedComponents"])
    return (filteredGraphConnectedComponents > connectedComponents)


def isBridge(self, edge):
    """
    Verifica se uma aresta é uma ponte.

    Percorre as componentes conexas do grafo, filtrando as componentes conexas
    em detrimento da aresta. Se o número de componentes filtradas for maior do
    que o número de componentes originais, então a aresta é uma ponte.

    Args:
        edge (string): aresta a ser verificada como ponte.

    Returns:
        boolean: True se o nó em questão for uma ponte; False caso contrário.

    Raises:
        None
    """

    connectedComponents = len((self.depthFirstSearch())["connectedComponents"])
    filteredGraph = self.filteredEdge(edge)
    filteredGraphConnectedComponents = len((filteredGraph.depthFirstSearch())["connectedComponents"])
    return (filteredGraphConnectedComponents > connectedComponents)
