# graph
Python Graph Library


# Desenvolvimento
## Subir container e acessá-lo
```bash
docker-compose run runner bash
```

## Instalar pacote localmente e atualizar mudanças
```bash
pip install -e .
```

### Pacotes externos
Ao utilizar um pacote externo deve-se adicioná-lo no install_requires que está no setup.py


## Executando Testes
```bash
python setup.py test
```

### Em um container separado
```bash
docker-compose -p tests run --rm test
```
