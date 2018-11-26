#!/usr/bin/env python
# -*- coding: utf-8 -*-

from memoize import Memoize
import numpy
import re


@Memoize
def formatEdgeString(node1, node2):
    """
    Gera uma string que representa um aresta.

    Recebe dois inteiros (dois vértices do grafo), e o formata com a notação de
    aresta a-b onde a é o vértice de menor valor, e b o de maior.

    Args:
        node1 (int): número de um dos vértices ligados à aresta
        node2 (int): número de um dos vértices ligados à aresta

    Returns:
        str: aresta no formato "a-b"

    Raises:
        TypeError: caso os argumentos não sejam do tipo inteiro
    """

    if not(isinstance(node1, int)) or not(isinstance(node2, int)):
        raise TypeError('arguments node1 and node2 must be integers')
    return '{:d}-{:d}'.format(min(node1, node2), max(node1, node2))


@Memoize
def formatEdgeDestination(node1, node2):
    """
    Gera uma string que representa um arco node1->node2

    Recebe dois inteiros (dois vértices do grafo), e o formata com a notação de
    aresta a->b onde a é o vértice de origem, e b o de destino.

    Args:
        node1 (int): número de um dos vértices ligados à aresta
        node2 (int): número de um dos vértices ligados à aresta

    Returns:
        str: arco no formato "a->b"

    Raises:
        TypeError: caso os argumentos não sejam do tipo inteiro
    """

    if not(isinstance(node1, int)) or not(isinstance(node2, int)):
        raise TypeError('arguments node1 and node2 must be integers')
    return '{:d}->{:d}'.format(node1, node2)


@Memoize
def translateEdgeNotation(edgeText):
    """
    Interpreta uma aresta em formato de texto e retorna os seus vértices.

    Recebe uma string de uma aresta formatada, o intepreta, e retorna uma lista
    de seus vértices em valor inteiro.

    Args:
        edgeText (str): valor da aresta no formato texto "a-b"

    Returns:
        numpy.ndarray: lista de duas dimensoes de inteiros representando os
        vértices ligados à aresta

    Raises:
        TypeError: se o argumento fornecido não for uma string
        ValueError: se o argumento fornecido não estiver no formato "int-int"
    """

    if not(isinstance(edgeText, str)):
        raise TypeError('argument edgeText must be a string')
    if not(re.match(r'(\d+)-(\d+)', edgeText)):
        raise ValueError('argument edgeText must be in format NUM-NUM')
    return numpy.array(edgeText.split('-'), dtype=int)


def hasNegativeEdge(self):
    """
    Verifica se existe alguma aresta com valor negativo.

    Percorre todas as arestas do grafo em busca de alguma com valor negativo.

    Args:
        None

    Returns:
        Boolean: True se possuir aresta negativa; False em caso contrário

    Raises:
        None

    """

    for i in range(self.nodesAmount):
        for j in range(self.nodesAmount):
            if (self.valueMatrix[i][j] < 0):
                return True
    return False


def getAllEdges(self):
    """
    Obtém todas as arestas do grafo.

    Percorre a matriz de valores do grafo, inserindo todas as arestas do grafo
    formatadas no padrão [node1, node2, weight] em uma lista.

    Args:
        None

    Returns:
        edges (list): lista contendo todas as arestas do grafo, formatadas e não
        repetidas.

    Raises:
        None
    """

    edges = []
    for i in range(self.nodesAmount):
        for j in range(self.nodesAmount):
            if (self.valueMatrix[i][j] != 0):
                edge = [min(i, j), max(i, j), self.valueMatrix[i][j]]
                if edge not in edges:
                    edges.append(edge)
    return edges


def getAllArcs(self):
    """
    Obtém todos os arcos do grafo.

    Percorre a matriz de valores do grafo, inserindo todas os arcos do grafo
    formatadas no padrão [node1, node2, weight] em uma lista.
    Lembrando que uma aresta == 2 arcos de mesmo valor em
    direção opostas

    Args:
        None

    Returns:
        edges (list): lista contendo todos os arcos do grafo, formatados e não
        repetidas.

    Raises:
        None
    """

    arcs = []
    for i in range(self.nodesAmount):
        for j in range(self.nodesAmount):
            if (self.valueMatrix[i][j] != 0):
                arc = [i, j, self.valueMatrix[i][j]]
                if arc not in arcs:
                    arcs.append(arc)
    return arcs
