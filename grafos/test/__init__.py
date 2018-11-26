#!/usr/bin/env python
# -*- coding: utf-8 -*-

class TestFile(object):
    import grafos

    attributes = [
        "nodesAmount",
        "valueMatrix"
    ]

    methods = [
        "openFile",
        "readNodesAmount",
        "generateValueMatrix",
        "filteredNode",
        "filteredEdge",
        "order",
        "neighbors",
        "degree",
        "edgesAmount",
        "size",
        "isConnected",
        "isArticulation",
        "isBridge",
        "depthSearch",
        "depthFirstSearch"
    ]

    def test_attributesAvailable(self):
        for a in self.attributes:
            assert hasattr(self, a)

    def test_methodsAvailable(self):
        for m in self.methods:
            assert hasattr(self, m)
            assert callable(m)
