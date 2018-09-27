from graph import Graph
from os import path

dirname = path.dirname(__file__)
filePath = path.join(dirname, 'teste.txt')
graph1 = Graph(filePath)
# print(graph1.valueMatrix)
print(graph1.size())
print(graph1.neighbors(0))
print(graph1.degree(0))
