class Graph(object):
    from .file import openFile, readNodesAmount
    from .matrix import generateValueMatrix
    from .basic import order, neighbors, degree, edgesAmount, size

    """Graph Main class """
    def __init__(self, filePath):
        super(Graph, self).__init__()
        self.filePath = filePath
        self.valueMatrix = None
        self.nodesAmount = None
        self.generateValueMatrix()
