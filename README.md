# graph
Python Graph Library 0.1

## Subir container e acessá-lo
```bash
docker-compose run runner bash
```

## Instalar pacote localmente e atualizar mudanças
```bash
pip install -e .
```

## Instalar dependências
```bash
python setup.py develop
```

### Pacotes externos
Ao utilizar um pacote externo deve-se adicioná-lo no install_requires que está no setup.py


## Executando Testes
docker-compose -p tests run --rm test
