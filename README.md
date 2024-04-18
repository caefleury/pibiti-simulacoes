# PIBITI - SIMULACOES

Repositório com as simulações do projeto de PIBITI focado em simulações termodinâmicas em estruturas nanomoleculares.

### Título do projeto : Propriedades Físicas de Sistemas Nanoestruturados na Presença de Defeitos

- Início: Setembro 2023
- Fim: Setembro 2024

## Objetivos:

- Criar a célula unitário do R10-Graphene em arquivo .xyz
- Gerar a estrutura padrão de uma folha de R10-Grapehene com um script genético
- Gerar estruturas com rasgos (nanocracks)

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

### set – Setting the unitcell parameters

To be able to work correctly, all other procedures of the PBCTools plugin require the VMD unitcell parameters to be set. Some file formats and their readers provide the necessary information (e.g. the DCD, VTF and Amber crdbox formats). When the format does not provide the information, the parameters can either be set with help of the command pbc set, or they can be read in from a file in XST format via the procedure pbc readxst (see section 5).

### Syntax:

```
pbc set cell [options…]
```
### Description:

Sets the VMD unit cell properties to cell in the specified frames. cell must either contain a single set of unit cell parameters that will be used in all frames of the molecule, or it must contain a parameter set for every frame.

### Example

  Set the unit cell side length to 10 in all frames:

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

- em x:  a * replicações em x = 6.3028 * 17 = 107.1476
- em y:  b * replicações em y = 4.9302 * 21 = 103.5342
- em z:  z = 100



  ```
  pbc set {107.1476 103.5342 100.0}
  ```


  ## Padrão de pastas para simulação LAMPPS

  ### Uma pasta de simulação LAMPPS precisa de 3 arquivos 
  1. Arquivo .charge da estrutura
  2. Arquivo .reaxff
  3. Arquivo da strain (strain-x ou strain-y)
