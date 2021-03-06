#!/usr/bin/env python
# -*- coding: utf-8 -*-

from grafos import Graph
from os import path
dirname = path.dirname(__file__)


def testInputGraph(i):
    print("\n\n \t Carregando Grafo ", i, "\n\n")
    graph = Graph(path.join(dirname, 'grafo{:d}.txt'.format(i)))

    print('\tTAMANHO: {}\n'.format(graph.size()))
    with open(path.join(dirname, '../output/dadosDoGrafo{:d}.txt'.format(i)), 'w+') as f:
        f.write('Tamanho do Grafo: {}\n'.format(graph.size()))
        f.write('Vizinhos do vértice 1: {}\n'.format(graph.neighbors(0)))
        f.write('Grau do vértice 1: {}\n'.format(graph.degree(0)))
        f.write('É bipartido: {}\n'.format(graph.isBipartite()))
        f.write('É euleriano?: {}\n'.format(graph.isEulerian()))
        f.write('Circuito Euleriano: {}\n'.format(graph.hierholzer()))
        f.write('Resultado Árvore Geradora Minima: {}\n'.format(graph.kruskal()))
        f.write('Busca de Conjunto Independente: {}\n'.format(graph.findStableSet()))
        f.write('Busca em Profunidade: {}\n'.format(graph.depthFirstSearch()))
        f.write('Busca em Largura: {}\n'.format(graph.bellmanFord()))
        f.write('É conexo?: {}\n'.format(graph.isConnected()))
        f.write('O vértice 1 é articulação?: {}\n'.format(graph.isArticulation(0)))
        f.write('A aresta 3-4 é ponte?: {}\n'.format(graph.isBridge('3-4')))
        f.write('Possui circuito negativo?: {}\n'.format(graph.hasNegativeCircuit()))


def testHurricane():
    hurricane = Graph(path.join(dirname, 'hurricane.txt'))
    tree = hurricane.kruskal()
    print("\nÁrvore: ", tree)


if __name__ == "__main__":
    testInputGraph(1)
    testHurricane()
