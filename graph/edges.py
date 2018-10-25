import numpy


def formatEdgeString(node1, node2):
    return '{:d}-{:d}'.format(min(node1, node2), max(node1, node2))


def translateEdgeNotation(edgeText):
    return numpy.array(edgeText.split('-'), dtype=int)
