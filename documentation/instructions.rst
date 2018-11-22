Instruções
************

Requisitos
-----------
Você precisa ter o **Python 3.\*** e, preferencialmente o `Pip <https://pypi.org/project/pip>`_


Instalação
-----------
Para instalar o pacote, após baixar o código fonte basta rodar o comando `pip install .`.

Se tiver baixando este pacote externamente, pelo pip, basta executar `pip install graph`


Desenvolvedores
-----------------

Subir container e acessá-lo
============================
.. code-block:: bash

   docker-compose run runner bash

Instalar pacote localmente e atualizar mudanças
==================================================
.. code-block:: bash

   pip install -e .

Pacotes externos
============================
Ao utilizar um pacote externo deve-se adicioná-lo no install_requires que está no setup.py


Executando Testes
============================
.. code-block:: bash

   python setup.py test

Em um container separado

.. code-block:: bash

   docker-compose -p tests run --rm test
