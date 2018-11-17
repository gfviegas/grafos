class Graph(object):
    from .file import openFile, readNodesAmount, writeGraphOnFile
    from .matrix import generateValueMatrix, filteredNode, filteredEdge
    from .edges import getAllEdges
    from .basic import order, neighbors, degree, edgesAmount, size, isConnected, isEulerian, isArticulation, isBridge
    from .search import depthSearch, depthFirstSearch, isBipartite, bellmanFord, hasNegativeCircuit
    from .features import hierholzer, searchHierholzer, kruskal, kruskalUnion, kruskalFind

    """Graph Main class """
    def __init__(self, filePath=None):
        self.filePath = filePath
        self.valueMatrix = None
        self.nodesAmount = None
        if (filePath is not None):
            self.generateValueMatrix()
