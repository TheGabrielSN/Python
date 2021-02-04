#
"""
Obs: Arquivo apenas informacional, não é recomendado a execução do mesmo, pois pode
apresentar alguma mensagem de erro por conta da forma de apresentação
"""
#

"""
ao usar uma função e colocar algo dentro dos (), é dito que a função está recebendo
parametros.
int(10), o parametro da função int() é o número 10
print("arquivo"), o parametro da função print() é o texto arquivo.
"""

#########               Variaveis                ##############
""" int - inteiro (0 1 10 100 ...)
float - ponto flutuante (0.5 1.2515 5.4611 2.1415 ...)
str "string" - texto (asfsdv fsda afsd) obs: sempre acompanhado por ""
bool "booleano" - valor logico (verdadeiro ou falso / True - False)
-----------------------------------------------------------------------------
nome de variavel:
- não se pode começar com número
- não se pode ter caracteres especiais (ç ^ ~ ´ ! = ...)
- não de pode ter espaços
- funções do proprio python (int, float, print, list ...)
- exemplos de nomes validos:
          lista
          nomePessoa
          nome_Pessoa
          usuario1
          arquivos
          comecar (começar é invalido)
"""

num = 10 #tipo int
nome = "Meu nome"  #tipo str
ligado = True #bool
x = 5.5 #tipo float

#########               Entrada de dados                ##############
"""função input():
Propria do python para receber dados do terminal de comandos ao executar algum código.
Por padrão, todo dado é recebido como string, ou sejam precisa ser convertido para outros
valores quando necessario.
O tipo da entrada vai ser delimitado de acordo com o tipo de variaives decidido para a conversão.
ao usar int(input()), o python vai pegar o texto digitado e converter para um número inteiro.
Para int(input()):
    Recebe qualquer número inteiro
    Converte qualquer número float para inteiro
    Não recebe texto
Para float(input()):
    Recebe qualquer número float
    Converte qualquer número inteiro para float
    Não recebe texto
Para str(input()) ou apenas input:
    Recebe qualquer dado na forma de texto, ou seja, ao colocar um número, o python vai interpretar
    como um texto.
Para bool(input()):
    Qualquer dado digitado vai dar True (verdadeiro).
"""
x = int(input()) #vai receber um número inteiro digitado ao executar o programa
x = float(input()) #vai receber um número de ponto flutuante (quebrado) digitado ao executar o programa
x = str(input()) ou x = input() #vai receber um texto digitado ao executar o programa

#########               Conversão de dados                ##############
"""A conversão entre dados em python é comun e facil, basta usar o tipo de variaveis já existentes.
obs.: type = tipo (traduzido do inglês)
Regras:
- Texto só pode ser convertido para número em caso de o texto ser apenas o número, palavras não podem
ser convertidas para numero
- Ao converter uma string para um número float para int, ele sempre arredonda para o número abaixo,
ou seja, é feita a eliminação das casas decimais e não considerada a regra de arredondamento.
Para o texto "2.5" (type str):
    é possível converter para float e para int: 
        float("2.5") -> 2.5 type float
        int("2.5") -> 2 type int
Para o numero 10 (type int):
    é possível converter para float e para str: 
        float(10) -> 10.0 type float
        str(10) -> "10" type str
Para o numero 2.1415 (type float):
    é possível converter para str e para int: 
        str(2.1415) -> "2.1415" type str
        int(2.1415) -> 2 type int

"""
num = int("2"); num = int(2.5)
num = float(2); num = float("2")
num = str(2); num = str(2.5)

#########               Impressão de dados                ##############
"""Função print() do python.
inicialmente, o print() imprime qualquer coisa em formar de texto na tela.
    print("Python") -> irá aparecer na tela a palavra Python.
Em muitos casos, se há algo para fazer para o print apresentar alfo para fazer.
    print(2+2) -> a saída será 4, pois se trata de uma operação matemática
    
    print("2+2") -> a saíra será 2+2, pelo fato de "" representar texto
    
    num = 10
    print(num) -> a saída será 10, pois o print está recebendo uma variaveil como parametro.
    
    print("X =", num) - a saída será X = 10, pois está sendo passado um texto e uma variavel,
    ao usar a , o print adiciona um espaço.
    
    print("X = %d" %num), o % é usado para ditar onde uma variavel vai ficar no texto, %d para int, 
    %f para float e %s para string. Obs.: ao usar %f, é possível dizer o número de casas decimais 
    colocando %.2f (duas casas decimais, o .n define o número de casas decimais, onde n é um número
    inteiro)

    print("X = {}".format(num)), o .format() é uma função para editar texto e utiliza os {} para 
    marcar no texto a posição da variavel de qualquer tipo. Obs.: para ditar a quantidade de 
    casas decimais, é utilizado {:.2f} com o mesmo funcionamento do %f.
    dentro de um print é possivel colocar quantos {} desejar, onde cada um se refere a uma
    variavel.

    print(f"Primeiro número: {num}, Segundo número{num+1}"), sendo uma variação do .format esse
    metodo visa simplificar a impressão de variaveis.
"""
print(2*2*2) #saida 8
print("Texto aleatorio") #saida Texto aleatorio
num = 100
print("%d" %num) #saida 100
print("filler:", num) #saida filler: 100
print("{} {}".format(num, num)) #saida 100 100
print(f"Primeiro número: {num}, Segundo número {num+1}") #saida Primeiro número: 100, Segundo número 101

