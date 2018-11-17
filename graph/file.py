import numpy

def openFile(self):
    if (not hasattr(self, 'filePath') or not isinstance(self.filePath, str)):
        raise Exception('filePathNotDefined')

    self.file = open(self.filePath, 'r')


def readNodesAmount(self):
    self.nodesAmount = int(self.file.readline())


def writeGraphOnFile(graph, nodesAmount, info, fileName):
    """
    Escreve os dados de um grafo qualquer em um arquivo externo.

    Args:
        graph (list): lista de vértices e pesos do grafo, em formato padrão.
        nodesAmount (int): quantidade de vértices do grafo.
        info (list): lista de elementos extras a serem escritos no fim do arquivo.
        fileName (str): nome do arquivo de destino.

    Returns:
        None

    Raises:
        Exception: filePathNotDefined caso o nome do arquivo não seja do tipo
        string.
    """

    if not isinstance(fileName, str):
        raise Exception('filePathNotDefined')

    # Abre o arquivo para escrita:
    file = open(fileName, "w")

    # Escreve o número de nós:
    file.write(str(nodesAmount) + "\n")

    # Escreve o grafo no formato u v w (dois vértices e o peso da aresta):
    for u, v, w in graph:
        file.write(str(u + 1) + " " + str(v + 1) + " " + str(w) + "\n")

    # Escreve informações extras passadas como parâmetro:
    for i in info:
        file.write(str(i) + "\n")

    file.close()
