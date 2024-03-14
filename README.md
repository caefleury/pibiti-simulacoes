# PIBITI - SIMULACOES

Repositório com as simulações do projeto de PIBITI focado em simulações termodinâmicas em estruturas nanomoleculares.

### Título do projeto : Propriedades Físicas de Sistemas Nanoestruturados na Presença de Defeitos

- ### Início: Setembro 2023
- ### Fim: Setembro 2024

## Objetivos:

- Criar a célula unitário do R10-Graphene em arquivo .xyz
- Gerar a estrutura padrão de uma folha de R10-Grapehene com um script genético
- Gerar estruturas com rasgos (nanocracks)

## Configurações iniciais

### Configuração do PYTHONPATH

Acesse o ~/.bashrc

```
nano ~/.bashrc
```

Adicione os caminhos ao PYTHONPATH: No final do arquivo .bashrc, adicione as linhas para exportar os pacotes

```
export PYTHONPATH=$PWD/src/utils
```

Subistituir `$PWD` pelo caminho até o repositorio. Exemplo: `/home/my_user/.../<nome_do_repositorio>`

## Como rodar o arquivo genético:

Em src/scripts/replicate.py altere número de replicações em cada direção mudando o valor das variáveis `n_replications_x` e `n_replications_y`:

```
n_replications_x = 17 # alterar replicações na direção x
n_replications_y = 19 # alterar replicações na direção y
```

Acessar a pasta e executar o arquivo replicate.py:

```
python3 replicate.py
```

## Como rodar os arquivos com rasgos:

Em src/scripts acesse os arquivos n1_nanocrack e n2_nanocrack e altere número de replicações em cada direção mudando o valor das variáveis `n_replications_x` e `n_replications_y`:

```
n_replications_x = 17 # alterar replicações na direção x
n_replications_y = 19 # alterar replicações na direção y
```

Para mudar o tamanho do rasgo central altere o valor da varíavel `crack_size`:

```
crack_size = 9 # alterar o tamanho do rasgo
```

Acessar a pasta e executar o arquivo com a simulação do rasgo:

```
python3 <nome_do_arquivo>.py
```
