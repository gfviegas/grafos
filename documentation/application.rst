Aplicação na Vida Real
****************
A teoria dos grafos é um ramo da matemática que estuda as relações entre os objetos de um determinado conjunto.
Para tal são empregadas estruturas chamadas de grafos, **G(V,E)**, onde **V** é um conjunto não vazio de
objetos denominados vértices (ou nós) e **E** (*edges*) é um subconjunto de pares não ordenados de V.
Uma Árvore Geradora Mínima (MST) de G é qualquer árvore geradora de G que possua custo mínimo. A aplicação
na Vida Real propõe a existência de um grafo G cujos vértices representem cidades e/ou pontos importantes
da região metropolitana de Belo Horizonte. Devido à aproximação de um furacão, soldados precisam obter uma rota
de acesso a todos os pontos, percorrendo a menor distância possível no menor tempo. O peso das arestas do grafo
representam o tempo levado no percurso entre um ponto e outro, em minutos. A imagem abaixo descreve o grafo completo:

.. image:: _static/hurricane/hurricaneGraph.png

O algoritmo de MST implementado na biblioteca **Graph** forneceu a seguinte MST, com custo total de 601.0 min:

.. image:: _static/hurricane/hurricaneTree.png
