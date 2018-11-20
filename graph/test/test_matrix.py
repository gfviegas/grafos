#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path
import pytest
import numpy
# from ..file import readNodesAmount as RNA


@pytest.fixture(scope="module")
def testFile():
    dirname = path.dirname(__file__)
    yield path.join(dirname, 'graph0.txt')


class TestFile(object):
    from ..file import openFile
    from ..matrix import generateValueMatrix, filteredEdge, filteredNode

    def readNodesAmount(self):
        self.nodesAmount2 = int(self.file.readline())

    @pytest.fixture(autouse=True)
    def requestFilePath(self, testFile):
        self.filePath = testFile
        yield testFile
        self.filePath = None

    # Tests begin
    def test_valueMatrixInvalid(self):
        self.nodesAmount = None
        assert not hasattr(self, 'valueMatrix')
        with pytest.raises(Exception, match='nodesAmountNotDefined'):
            self.generateValueMatrix()

    def test_valueMatrixValid(self):
        self.nodesAmount = 5
        self.generateValueMatrix()
        assert isinstance(self.valueMatrix, numpy.ndarray)
        for line in self.valueMatrix:
            assert isinstance(line, numpy.ndarray)
            for column in line:
                assert isinstance(column, numpy.float)

    def test_mainDiagonalValid(self):
        self.nodesAmount = 5
        self.generateValueMatrix()
        for idx in range(0, self.nodesAmount):
            assert self.valueMatrix[idx][idx] == 0

    def test_filteredNode(self, requestFilePath):
        from graph import Graph
        graphTested = Graph(requestFilePath)
        filtered = graphTested.filteredNode(0)
        assert (filtered.order() < 5)

    def test_filteredEdge(self, requestFilePath):
        from graph import Graph
        graphTested = Graph(requestFilePath)
        filtered = graphTested.filteredEdge("1-2")
        assert (len(graphTested.neighbors(0)) > len(filtered.neighbors(0)))
        assert (1 not in filtered.neighbors(0))
        assert (filtered.valueMatrix[0][1] == 0.0)
