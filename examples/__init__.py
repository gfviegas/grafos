from graph import Graph
from os import path

dirname = path.dirname(__file__)


def testGraph1():
    graph = Graph(path.join(dirname, 'teste.txt'))
    print(graph.size())
    print(graph.neighbors(0))
    print(graph.degree(0))


def testGraphDisconnected():
    graphDis = Graph(path.join(dirname, 'disconnected.txt'))
    print(graphDis.isConnected())
    graphCon = Graph(path.join(dirname, 'connected.txt'))
    print(graphCon.isConnected())
    print(graphCon.isArticulation(1))


testGraphDisconnected()
