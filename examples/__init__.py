from graph import Graph
from os import path

dirname = path.dirname(__file__)
filePath = path.join(dirname, 'teste.txt')
graph1 = Graph(filePath)
print(graph1.valueMatrix)
