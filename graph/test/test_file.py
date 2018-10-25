from os import path
from io import TextIOWrapper
import pytest


@pytest.fixture(scope="module")
def testFile():
    dirname = path.dirname(__file__)
    yield path.join(dirname, 'graph0.txt')


class TestFile(object):
    from ..file import openFile, readNodesAmount

    @pytest.fixture(autouse=False)
    def requestFilePath(self, testFile):
        self.filePath = testFile
        yield testFile
        self.filePath = None

    # Tests begin
    def test_openFileInvalid(self):
        assert not hasattr(self, 'filePath')
        with pytest.raises(Exception, match='filePathNotDefined'):
            self.openFile()

    def test_openFileInexistent(self):
        self.filePath = 'inexistente'
        with pytest.raises(FileNotFoundError) as error:
            self.openFile()
        self.filePath = None

    def test_openFileValid(self, requestFilePath):
        self.openFile()
        assert isinstance(self.file, TextIOWrapper)
