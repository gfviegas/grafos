#!/usr/bin/env python
# -*- coding: utf-8 -*-

from graph import Graph
from os import path
import gc

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


def testAllGraphs():
    for i in [1, 3, 2, 4, 5]:
        testInputGraph(i)
        gc.collect()


def testHurricane():
    hurricane = Graph(path.join(dirname, 'hurricane.txt'))
    tree = hurricane.kruskal()
    print("\nÁrvore: ", tree)


grafo1 = Graph(path.join(dirname, 'grafo1.txt'))
ap1 = Graph(path.join(dirname, 'ap1.txt'))
ap2 = Graph(path.join(dirname, 'ap2.txt'))

# print(grafo1.order())
# print(grafo1.size())
# print(grafo1.neighbors(9))
# print(grafo1.degree(9))
# print(grafo1.bellmanFord(0)["distances"][9])
# print(grafo1.bellmanFord(0))
# print(grafo1.breadthFirstSearch())
# print(grafo1.depthFirstSearch())
# print(grafo1.kruskal())


# print(ap1.isArticulation(2))
# print(ap1.isBridge('2-3'))
# print(ap1.isBridge('0-1'))
# print(len(ap1.depthFirstSearch()["connectedComponents"]))
# print(ap1.hasNegativeCircuit())
# print(ap1.findStableSet())

print(ap2.isEulerian())
print(ap2.isBipartite())




# print(ap1.isArticulation(1))
# print(ap1.isArticulation(3))
# print(ap1.kruskal())
# print(ap1.isBipartite())
# print(ap2.isBipartite())
