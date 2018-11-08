class Graph(object):
    from .file import openFile, readNodesAmount
    from .matrix import generateValueMatrix, filteredNode, filteredEdge
    from .edges import getAllEdges
    from .basic import order, neighbors, degree, edgesAmount, size, isConnected, isArticulation, isBridge
    from .search import depthSearch, depthFirstSearch, isBipartite, bellmanFord, hasNegativeCircuit

    """Graph Main class """
    def __init__(self, filePath=None):
        self.filePath = filePath
        self.valueMatrix = None
        self.nodesAmount = None
        if (filePath is not None):
            self.generateValueMatrix()
