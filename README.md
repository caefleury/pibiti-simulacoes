# PIBITI - SIMULACOES

Repositório com as simulações do projeto de PIBITI focado em simulações termodinâmicas em estruturas nanomoleculares.

### Título do projeto : Propriedades Físicas de Sistemas Nanoestruturados na Presença de Defeitos

- Início: Setembro 2023
- Fim: Setembro 2024

## Objetivos:

- Criar a célula unitária do R10-Graphene em arquivo .xyz
- Gerar a estrutura padrão de uma folha de R10-Grapehene com um script genético
- Gerar estrutura pristine e estruturas com rasgos (nanocracks).
- Simular deformações utilizando o LAMMPS.
- Analisar os dados das deformações e indicar as propriedades termodinâmicas das estruturas.

## Configurações iniciais

### Configurando o PYTHONPATH Localmente

Acesse o ~/.bashrc

```
nano ~/.bashrc
```

Adicione os caminhos ao PYTHONPATH: No final do arquivo .bashrc, adicione as linhas para exportar os pacotes

```
export PYTHONPATH=$PWD/src/utils
```

Subistituir `$PWD` pelo caminho até o repositorio. Exemplo: `/home/my_user/.../<nome_do_repositorio>`

### Configuração do PYTHONPATH em ambiente virtual

1.  `python3 -m venv venv`
2.  `source ./venv/bin/activate`

## Como rodar o arquivo genético:

Em src/scripts/replicate.py altere número de replicações em cada direção mudando o valor das variáveis `n_replications_x` e `n_replications_y`:

```
n_replications_x = 17 # alterar replicações na direção x
n_replications_y = 21 # alterar replicações na direção y
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

## VMD Scripting

### set – Definindo os parâmetros da célula unitária

Para que funcione corretamente, todos os outros procedimentos do plugin PBCTools requerem que os parâmetros da célula unitária do VMD sejam definidos. Alguns formatos de arquivo e seus leitores fornecem as informações necessárias (por exemplo, os formatos DCD, VTF e Amber crdbox). Quando o formato não fornece a informação, os parâmetros podem ser definidos com a ajuda do comando pbc set, ou podem ser lidos de um arquivo no formato XST através do procedimento pbc readxst.

### Sintaxe:

```
pbc set cell [options…]
```

### Descrição:

Define as propriedades da célula unitária do VMD como cell nos quadros especificados. A cell deve conter ou um único conjunto de parâmetros da célula unitária que será usado em todos os quadros da molécula, ou deve conter um conjunto de parâmetros para cada quadro.

### Example

Definir o comprimento do lado da célula unitária como 10 em todos os quadros:

```
pbc set {10.0 10.0 10.0}
```

### Uso na simulação:

O tamanho da caixa deve refletir o tamanha da estrutura.O calculo pode ser feito com os valores das lattice constants e o número de replicações. Para o valor de z podemos atribuir 100.

Para as estruturas nesse projeto temos que:

- a (eixo x) = 6.3028
- b (eixo y) = 4.9302

Para o número de replicações temos que:

- eixo x = 17
- eixo y = 21

Portanto, nossa caixa de simulação terá os seguintes valores:

- em x: a _ replicações em x = 6.3028 _ 17 = 107.1476
- em y: b _ replicações em y = 4.9302 _ 21 = 103.5342
- em z: z = 100

  ```
  pbc set {107.1476 103.5342 100.0}
  ```

  ## Padrão de pastas para simulação LAMPPS

  ### Uma pasta de simulação LAMPPS precisa de 3 arquivos

  1. Arquivo .charge da estrutura
  2. Arquivo .reaxff
  3. Arquivo da deformação (strain-x ou strain-y)
