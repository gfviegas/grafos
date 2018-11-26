#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy


def openFile(self):
    """
    Abre o arquivo externo que contém as informações do grafo para leitura.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: filePathNotDefined caso o nome do arquivo não seja do tipo
        string.
    """

    if (not hasattr(self, 'filePath') or not isinstance(self.filePath, str)):
        raise Exception('filePathNotDefined')

    self.file = open(self.filePath, 'r')


def readNodesAmount(self):
    """
    Obtém o número total de nós do grafo.

    Lê a primeira linha do arquivo (que representa o número de nós) e a associa
    ao atributo nodesAmount do objeto.

    Args:
        None

    Returns:
        None

    Raises:
        None
    """

    self.nodesAmount = int(self.file.readline())


def writeGraphOnFile(graph, nodesAmount, info, fileName):
    """
    Escreve os dados de um grafo qualquer em um arquivo externo.

    Args:
        graph (list): lista de vértices e pesos do grafo, em formato padrão.
        nodesAmount (int): quantidade de vértices do grafo.
        info (list): lista de elementos extras a serem escritos no fim do arquivo.
        fileName (str): nome do arquivo de destino.

    Returns:
        None

    Raises:
        Exception: filePathNotDefined caso o nome do arquivo não seja do tipo
        string.
    """

    if not isinstance(fileName, str):
        raise Exception('filePathNotDefined')

    # Abre o arquivo para escrita:
    file = open(fileName, "w")

    # Escreve o número de nós:
    file.write(str(nodesAmount) + "\n")

    # Escreve o grafo no formato u v w (dois vértices e o peso da aresta):
    for u, v, w in graph:
        file.write(str(u + 1) + " " + str(v + 1) + " " + str(w) + "\n")

    # Escreve informações extras passadas como parâmetro:
    for i in info:
        file.write(str(i) + "\n")

    file.close()
