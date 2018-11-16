from .edges import formatEdgeString
import numpy
import itertools


def isEulerian(self):
    """
    Verifica se o grafo é Euleriano.

    Verifica se o grafo é conexo. Se sim, verifica se o grau de cada vértice
    do grafo é par (Teorema de Euler). Em caso afirmativo para as duas afirmações,
    conclui-se que o grafo é Euleriano.

    Args:
        None

    Returns:
        Boolean: True se o grafo for Euleriano; False em caso contrário

    Raises:
        None
    """

    if not self.isConnected(): return False

    for v in range(self.nodesAmount):
        if self.degree(v) % 2 != 0: return False

    return True


def searchHierholzer(self, node, root, subpath, edgesTraversed):
    """
    Busca por todos os vértices não visitados a partir de node.

    Realiza uma busca a partir do vértice parâmetro (node) até que a cadeia se
    complete no vértice inicial root. Nenhum elemento é inserido na lista edgesTraversed
    se todas as arestas que ligam o vértice node em seus vizinhos forem visitadas.

    Args:
        node (int): índice do vértice cujos vizinhos serão percorridos
        root (int): índice do vértice de início do caminho
        subpath (list): lista de vértices do subcaminho euleriano
        edgesTraversed (dictionary): lista de vértices do caminho euleriano completo

    Returns:
        None

    Raises:
        None
    """

    # Procura todos os vizinhos do vértice do parâmetro;
    neighbors = self.neighbors(node)

    # Verifica se o vértice já foi visitado e o adiciona na lista do subcaminho:
    for n in neighbors:
        edge1 = formatEdgeString(node, n)
        edge2 = formatEdgeString(n, node)
        if edge1 not in edgesTraversed or edge2 not in edgesTraversed:
            edgesTraversed[edge1] = edgesTraversed[edge2] = True
            subpath.append(n)
            if n == root: return
            else: self.searchHierholzer(n, root, subpath, edgesTraversed)


def hierholzer(self, node=0):
    """
    Algoritmo de Hierholzer para encontrar um Caminho Euleriano fechado em um
    grafo não direcionado, se o mesmo existir.

    Verifica se o grafo é Euleriano. Se sim, forma subcadeias fechadas a cada
    iteração, até que todas as arestas sejam visitadas. As subcadeias são
    unidas a fim de construir a cadeia principal.

    Args:
        node (int): nó inicial a ser utilizado pelo algoritmo, definido como zero por padrão.

    Returns:
        chain (list): lista de vértices da cadeia ou None se o grafo não for Euleriano.

    Raises:
        None
    """

    # Verifica se o grafo é um grafo Euleriano:
    if not self.isEulerian(): return None

    # Cria as estruturas de dados necessárias:
    chain = [node]
    traversed = {}
    pointer = 0

    # Percorre o grafo em busca de cadeias fechadas:
    while (len(traversed) // 2) < self.edgesAmount() and pointer < len(chain):
        subpath = []
        self.searchHierholzer(chain[pointer], chain[pointer], subpath, traversed)
        if len(subpath) != 0: chain = list(itertools.chain(chain[:pointer+1], subpath, chain[pointer+1:]))
        pointer += 1

    # Retorna a cadeia Euleriana fechada do grafo:
    return chain
