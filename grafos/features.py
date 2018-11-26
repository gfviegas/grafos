#!/usr/bin/env python
# -*- coding: utf-8 -*-

from memoize import Memoize
from .edges import formatEdgeDestination
from .file import writeGraphOnFile
from operator import itemgetter
from random import randint
import itertools


@Memoize
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
        edge1 = formatEdgeDestination(node, n)
        edge2 = formatEdgeDestination(n, node)
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


def kruskalFind(self, parent, i):
    """
    Método utilitário utilizado para encontrar um conjunto de um elemento i
    em uma sub-árvore.

    Args:
        parent (list): lista de nós da árvore
        i (int): índice da lista

    Returns:
        i (int): valor inteiro que representa um conjunto de elementos 'i'

    Raises:
        None
    """

    if parent[i] == i: return i
    return self.kruskalFind(parent, parent[i])


def kruskalUnion(self, parent, rank, x, y):
    """
    Método utilitário que realiza a união de dois elementos (vértices) x e y.

    Args:
        parent (list): Lista de vértices pais.
        rank (list): Estrutura de dados auxiliar.
        x (int): Primeiro vértice da relação.
        y (int): Segundo vértice da relação.

    Returns:
        None

    Raises:
        None
    """
    xroot = self.kruskalFind(parent, x)
    yroot = self.kruskalFind(parent, y)

    # Anexa a menor árvore da raiz até o topo (União por rank).
    # Se os ranks são iguais, utiliza uma delas como raiz:
    if rank[xroot] < rank[yroot]: parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]: parent[yroot] = xroot
    else: parent[yroot] = xroot; rank[xroot] += 1


def kruskal(self):
    """
    Algoritmo de Kruskal para encontrar a Árvore Geradora Mínima de um grafo,
    se a mesma existir.

    Verifica se o grafo é conexo. Em caso afirmativo, ordena todas as arestas
    por ordem crescente de pesos e insere de forma gulosa as arestas na árvore
    final, sem formar ciclos. O resultado final é um conjunto de arestas que
    compõem a MST (Minimum Spanning Tree).

    Args:
        None

    Returns:
        mstEdges (list): lista de vértices ligadas por arestas com seus pesos
        que fazem parte da árvore geradora mínima ou None caso ela não exista.

    Raises:
        None
    """

    # Verifica se o grafo é conexo:
    if not self.isConnected(): return None

    # Cria as estruturas de dados necessárias:
    mstEdges = []; parent = []; rank = []; info = [0]
    allEdges = sorted(self.getAllEdges(), key = itemgetter(2))

    # Variáveis de índice para as arestas ordenadas (i) e para o mstEdges (e):
    i = e = 0

    # Cria subconjuntos com elementos individuais, um para cada nó:
    for node in range(self.nodesAmount):
        parent.append(node)
        rank.append(0)

    # Acessa (número de vértices - 1) arestas:
    while e < self.nodesAmount - 1:
        # Seleciona a aresta de menor peso e incrementa o índice i:
        u, v, w = allEdges[i]
        x = self.kruskalFind(parent, u)
        y = self.kruskalFind(parent, v)
        i += 1
        # Se a inclusão da atual aresta não causa ciclo, inclui-se a mesma
        # no resultado e incrementa o índice e:
        if x != y:
            e = e + 1
            mstEdges.append([u, v, w])
            info[0] += w
            self.kruskalUnion(parent, rank, x, y)

    # Escreve a árvore geradora mínima em um arquivo externo, juntamente com a
    # soma dos pesos:
    fileName = 'output/generatedmst{:d}_{:d}.txt'.format(randint(0, 99999), randint(0, 99999))
    writeGraphOnFile(mstEdges, len(mstEdges), info, fileName)

    return mstEdges


def findStableSet(self):
    """
    Determina o conjunto independente de um grafo não direcionado.

    Heurística gulosa que ordena todos os vértices em ordem decrescente de grau.
    Enquanto existirem vértices na lista, o vértice com maior grau é selecionado
    e removido juntamente com seus vizinhos da lista. O vértice é então inserido
    no conjunto independente e o número de independência é incrementado.

    Args:
        None

    Returns:
        results (dictionary): dicionário que contém a lista de vértices que
        compõem o conjunto independente do grafo e um inteiro que representa
        o número de independência. Retorna a lista vazia e o número de independência
        igual à zero se o conjunto não existir.

    Raises:
        None
    """

    # Estruturas de dados necessárias:
    results = {"stableSet": [], "independenceNumber": 0}; nodes = []

    # Ordena os vértices em ordem não crescente de graus:
    for i in range(self.nodesAmount):
        nodes.append([i, self.degree(i)])

    sortedNodes = sorted(nodes, key=itemgetter(1), reverse=True)

    # Constrói o conjunto independente:
    while len(sortedNodes):
        # Seleciona o vértice de maior grau e obtém seus vizinhos:
        neigbourhood = []
        node = sortedNodes[0]
        neigbourhood = self.neighbors(node[0])

        # Remove os vizinhos do vértice da lista:
        for u in neigbourhood:
            for v in sortedNodes:
                if v[0] == u: sortedNodes.remove(v)

        # Adiciona o vértice no conjunto e incrementa o número de independência:
        results["stableSet"].append(node[0])
        results["independenceNumber"] += 1
        sortedNodes.remove(node)

    return results
