import numpy
import re


def formatEdgeString(node1, node2):
    if not(isinstance(node1, int)) or not(isinstance(node2, int)):
        raise TypeError('arguments node1 and node2 must be integers')
    return '{:d}-{:d}'.format(min(node1, node2), max(node1, node2))


def translateEdgeNotation(edgeText):
    if not(isinstance(edgeText, str)):
        raise TypeError('argument edgeText must be a string')
    if not(re.match(r'(\d+)-(\d+)', edgeText)):
        raise ValueError('argument edgeText must be in format NUM-NUM')
    return numpy.array(edgeText.split('-'), dtype=int)
