#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import numpy
from ..edges import formatEdgeString, translateEdgeNotation


class TestFile(object):
    def test_translateEdgeStringArgumentType(self):
        with pytest.raises(TypeError):
            translateEdgeNotation(90)

    def test_translateEdgeStringArgumentFormat(self):
        with pytest.raises(ValueError):
            translateEdgeNotation('90a010º')
        with pytest.raises(ValueError):
            translateEdgeNotation('aaa22-2')

    def test_translateEdgeStringArgumentValid(self):
        nodes = translateEdgeNotation('2-3')
        assert len(nodes) == 2
        assert isinstance(nodes, numpy.ndarray)
        assert nodes[0] == 2
        assert nodes[1] == 3

    def test_formatEdgeStringArgumentType(self):
        with pytest.raises(TypeError):
            formatEdgeString([2], 2)
        with pytest.raises(TypeError):
            formatEdgeString(3, 'a')
        with pytest.raises(TypeError):
            formatEdgeString(3.4, 1)

    def test_formatEdgeStringArgumentValid(self):
        edge = formatEdgeString(3, 90)
        assert isinstance(edge, str)
        assert edge == '3-90'
        edge = formatEdgeString(93, 1)
        assert isinstance(edge, str)
        assert edge == '1-93'
