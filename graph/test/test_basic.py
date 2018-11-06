from os import path
import pytest


@pytest.fixture(scope="module")
def testFile():
    dirname = path.dirname(__file__)
    yield path.join(dirname, 'graph0.txt')


class TestFile(object):
    from ..file import openFile, readNodesAmount
    from ..matrix import generateValueMatrix
    from ..basic import order, neighbors

    @pytest.fixture(autouse=True)
    def fillMatrix(self, testFile):
        self.filePath = testFile
        self.generateValueMatrix()
        yield testFile
        self.filePath = None

    def test_order(self):
        self.valueMatrix = [[1, 1, 2], [1, 1, 3], [4, 2, 1]]
        order = self.order()
        assert isinstance(order, int)
        assert (order == 3)

    def test_neighbors(self, fillMatrix):
        neighbors = self.neighbors(0)
        assert isinstance(neighbors, list)
        assert (1 in neighbors)
        assert (2 in neighbors)
        assert (3 not in neighbors)
