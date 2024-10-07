# Teste-Target-Sistemas

Questões referentes ao teste de estágio da empresa Target Sistemas

## Conteúdo

 * [Questão 1](#Questão-1)
 * [Questão 2](#Questão-2)
 * [Questão 3](#Questão-3)
 * [Questão 4](#Questão-4)
 * [Questão 5](#Questão-5)


## Questão 1

- Simples questão que apresenta um algoritmo básico usando a estrutura de repetição While

## Questão 2

- Esse algoritmo é responsável por receber do usuário um valor inteiro positivo e analisar se esse valor pertence a sequência de Fibonnacci. Caso o valor faça parte da sequência será retornado uma mensagem informado o pertencimento. Caso contrário será enviado uma mensagem informando que o valor não faz parte da sequência.

### Estrutura do Algoritmo
- Contém 3 funções. 
- A primeira função recebe o valor do usuário se certificando, por meio de uma estrutura de exceção, se esse valor é válido como número inteiro. Caso seja um valor inteiro negativo, a função é encrregada por meio de uma estrutura If/Else de requisitar um valor inteiro positivo.
- A segunda função é encarregada de verificar se o número inteiro inserido é pertencente a sequência de Fibonnacci.
- Por último, a terceira função faz o papel de informar as saídas (se pertence ou não à sequência) ao usuário

## Questão 3

- Estrutura lógica responsável por analisar um arquivo Json referente ao faturamento de uma empresa e informar as saídas requisitas: o maior faturamento, o menor faturamento e os dias em que se faturou quantia maior que a média de faturamento mensal.

### Estrutura do Algoritmo
- Por meio da biblioteca pandas o arquivo Json foi lido e transformado em um dataframe. Em seguinte, os dias com valores nulos são desconsiderados e é obtido por meio de funções do pandas o valor máximo de faturamento, o valor mínimo de faturamento e a média de faturamento mensal.
- Depois de obtidos os valores, por meio de uma estrutura de repetição "For" é verificado em quantos dias o faturamento foi maior que a média.
- Por fim, é imprimido na tela, os dados requisitados.

## Questão 4

- Código responsável por analisar um array de dados referente ao faturamento por estado de uma distribuidora.

### Estrutura do Algoritmo
- Inicilamente é calculado por meio de uma estrutura de repetição "While" o total de faturamento mensal. Logo depois, utiliza-se de uma estrutura igual, para calcular a porcentagem de participação de cada estado no faturamento mensal.
- Enfim, é imprimido na tela o faturamento mensal total e a participação de cada estado.

## Questão 5

- Estrutura simples responsável por inverter determinada string inserida pelo usuário
