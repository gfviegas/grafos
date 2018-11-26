#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
from .edges import translateEdgeNotation


def generateValueMatrix(self):
    """
    Preenche a matriz de valor a partir dos dados de um arquivo.

    Lê o arquivo vinculado ao grafo e cria a sua matriz de valores. A matriz
    terá tamanho MxM onde M é a quantidade de vértices, valor lido na primeira
    linha do arquivo.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: nodesAmountNotDefined caso não tenha sido atribuído um valor
        para o tamanho M de quantidade de vértices
    """

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


def filteredEdge(self, edge):
    """
    Clona o grafo com uma aresta removida do grafo original e o retorna.

    A partir do grafo original, traduz a aresta que se deseja remover e
    retorna uma nova instância de grafo sem a aresta solicitada.

    Args:
        edge (str): valor da aresta no formato texto "a-b"

    Returns:
        Graph: cópia do grafo original sem uma aresta

    Raises:
        None
    """

    from grafos import Graph
    filteredMatrix = numpy.copy(self.valueMatrix)
    # edgeNodes = list(map(lambda e: e - 1, translateEdgeNotation(edge)))
    edgeNodes = list(map(lambda e: e, translateEdgeNotation(edge)))
    filteredMatrix[edgeNodes[0]][edgeNodes[1]] = 0
    filteredMatrix[edgeNodes[1]][edgeNodes[0]] = 0

    graph = Graph()
    graph.valueMatrix = filteredMatrix
    graph.nodesAmount = graph.order()

    return graph


def filteredNode(self, node):
    """
    Clona o grafo com um vértice removido do grafo original e o retorna.

    A partir do grafo original, remove os valores do vértice que se deseja
    remover e retorna uma nova instância de grafo sem o vértice solicitado e
    suas arestas.

    Args:
        node (int): índice do vértice que se deseja remover

    Returns:
        Graph: cópia do grafo original sem um vértice e suas arestas

    Raises:
        None
    """

    from grafos import Graph
    filteredMatrix = numpy.copy(self.valueMatrix)
    filteredMatrix = numpy.delete(filteredMatrix, node, 0)
    filteredMatrix = numpy.delete(filteredMatrix, node, 1)

    graph = Graph()
    graph.valueMatrix = filteredMatrix
    graph.nodesAmount = graph.order()

    return graph
