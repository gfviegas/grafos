from os import path
import pytest
# from ..file import readNodesAmount as RNA


@pytest.fixture(scope="module")
def testFile():
    dirname = path.dirname(__file__)
    yield path.join(dirname, 'graph0.txt')


class TestFile(object):
    from ..file import openFile
    from ..matrix import generateValueMatrix

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
        assert isinstance(self.valueMatrix, list)
        for line in self.valueMatrix:
            assert isinstance(line, list)
            for column in line:
                assert isinstance(column, int)

    def test_mainDiagonalValid(self):
        self.nodesAmount = 5
        self.generateValueMatrix()
        for idx in range(0, self.nodesAmount):
            assert self.valueMatrix[idx][idx] == 0
