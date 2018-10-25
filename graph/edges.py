import numpy
import re


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
