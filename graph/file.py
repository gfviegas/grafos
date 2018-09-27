def openFile(self):
    if (not hasattr(self, 'filePath') or not isinstance(self.filePath, str)):
        raise Exception('filePathNotDefined')

    self.file = open(self.filePath, 'r')


def readNodesAmount(self):
    self.nodesAmount = int(self.file.readline())
