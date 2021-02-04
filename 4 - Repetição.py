#
"""
Obs: Arquivo apenas informacional, não é recomendado a execução do mesmo, pois pode
apresentar alguma mensagem de erro por conta da forma de apresentação
"""
#

#########               while                ##############
"""
while (do inglês, enquanto) é uma condição para repetição de algum código
enquanto uma certa condição é verdadeira.
Exemplo:
x = 0
while(x!=1):
    print("zero")
    x = 1
Nesse exemplo, a print é executado enquanto a condição é verdadeira (ou seja, x
diferente de 1). Ao executar esse código, o x só é impresso uma vez, poís logo em seguida,
é atribuido 1 ao x.
Em resumo... Considerando:
l1 x = 0
l2 while(x!=1):
l3     print("zero")
l4     x = 1
l5

é executado  l1 (x é definido com o valor 0),
executa a l2 e se verifica a condição do while
(verifica se x!=1, assim como no if, caso True, é executado o codigo dentro do while, caso
False, o é pulado para fora do while),
pelo fato da condição ser verdadeira, é seguido para a linha l3 (imprime na tela o texto zero),
segue para l4 (onde é dito que x é igual a 1) e é dito que chegou ao fim do while,
então volta para l2 e se é verificado novamente a condição.

O while repete esse processo até que a sua condição seja falsa e a execução do programa 
continue.
Se for pego o exemplo dado antes e retirado o x = 1:

x = 0
while(x!=1):
    print("zero")

o while vai se tornar infinito, ou seja, sua condição nunca será falsa e o programa nunca saira 
dessa parte.
(Em python, existe um limite para a quantidade de vezes que algo pode ser executado em loop (repetição)
dito isso, vai chegar um momento em que o programa será fechado pelo sistema e irá apresentar uma
mensagem de erro)

Levando isso em conta, é sempre importante verificar a condição de parada do while, para que esse
problema não aconteça em algum código.
"""
x = 10
while(x>0):
    print("X é positivo")
    x -= 1

#########               else no while                ##############
"""
O while é parecido com o if, sua única diferença é a possibilidade de repetição de um mesmo
código.
Seguindo essa ideia, é possível fazer uma condição para quanto o while seja falso.

x = 10
while(x>0):
    print("Número {}, pertecente aos naturais positivos".format(x))
    x -= 1
else:
    print("Número nulo")

Aqui, o while será executado 10x, até q x seja igual a 0. Em seguida, será executado o código dentro
do else.
"""
num = int(input("Digite algum número"))
while(num%2 == 0):
    print("{} é par".format(num))
    num = num/3
else:
    print("Número de parada: {}".format(num))

#########               for                ##############
"""
for (do inglês, para) é utilizado para reproduzir um determinado bloco de instruções 
durante um determinado tempo especifico, ou seja, o bloco de código será executado
durante um periodo de tempo determinado por algum fator.
A sintaxi basica do for:
    for i in "palavras":, onde:
        for -> função de repetição
        i -> variavel criada para a execução do código
        in -> função que define de onde vem os dados
        "palavras" -> string que delimitará a repetição do laço for

> Quando executado o exemplo acima, o for vai varrer a string letra por letra.
>>funcionamento: a primeira letra da string é atribuida a variavel definida no for
e, em seguida, é executado o bloco de código do for. Ao finalizar o bloco, volta para
o inicio (ou seja, para o for), a segunda letra é atribuida a variavel e o bloco é
repetido, até o momento em que chegar no final da string.
exemplo:
for i in "texto":
    print(i)
>saida:
    t
    e
    x
    t
    o

> Utilização de números no for:
Para definir o periodo de repetição dentro do for utilizando número, é utilizado
a função range. range() recebe entre 1 e 3 parametros: range(inicio, fim, pulo)
inico é o número que se inicia a contagem.
fim representa o número que será finalizado a contagem.
pulo é o número que representa o número que será "somado" a cada ciclo do for.
exemplo:
for x in range(0, 10, 1):
    print(x)
> saida:
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
A saída só imprimiu até o 9 pelo fato do range só chegar até o número final -1 
([inicio, fim) -> da matematica: fechado no inicio e aberto no fim).

> os argumentos do range pode ser:
for x in range(10)

> onde o 10 representa o valor do fim, nesse modo, o inicio e o pulo recebem o valor
padrão, 0 para o inicio e 1 para o pulo.
a saida será: 0 1 2 3 4 5 6 7 8 9
for x in range(1,10)

> nesse caso, o 1 representa o inicio e 0 10 representa o fim, o pulo recebe o valor
padrão 1.
a saida será: 1 2 3 4 5 6 7 8 9
for x in range(0,10,2)

> nesse caso, o range está completo (com todos os seus argumentos), com isso o
0 representa o inicio, o 10 representa o fim e o 2 representa o pulo.
a saida será: 0 2 4 6 8
"""
soma = 0
for num in range(1, 10):
    soma += num
print("soma =",soma) #A saída será: soma = 45, pois foi feita a soma de todos os números
                     #entre 1 e 9

#########               Condição de parada                ##############
"""
As vezes é necessario parar alguma repetição antes de sua condição de parada seja atingida.
para isso é utilizado o comando break.
É possivel usar-ló tanto no while quanto no for.

x = 0
while(x>=0):
    print("Positivo")
    x = int(input())
    if(x > 100):
        print("valor alto")
        break
print("fim")
-----------------------------
for x in range(1000):
    if(x == 100):
        break
    print(x**0.5)
"""
while True:
    valor = input("Digite algo")
    print(valor.upper())
    if(valor == ""):
        break

#########               While ou For?                ##############
"""
Por mais que os dois possuam o mesmo proposito, existe algo que define qual usar cada um.
O While é utilizado para quando não se sabe o momento exato de para a execução, ou seja,
você sabe qual é a condição de parada, mas você não sabe quando essa condição acontecera.
Por conta disso, o while pode ser infinito.

Já o for é utilziado quando se sabe o momento de finalização. Por possuir um intervalo de
começo e fim, o for não pode ser infinito, assim, sendo previsivel o seu fim.

exemplo de uso do for: https://www.urionlinejudge.com.br/judge/pt/problems/view/1078
x=(int(input()))
for s in range(1,10+1):
    print("{} x {} = {}".format(s,x,s*x))

exemplo de uso do while: https://www.urionlinejudge.com.br/judge/pt/problems/view/1114
while True:
    senha=int(2002)
    x=int(input())
    if x==senha:
        print("Acesso Permitido")
        break 
    if x!=senha:
        print("Senha Invalida")
"""