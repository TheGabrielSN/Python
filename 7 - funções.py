#
"""
Obs: Arquivo apenas informacional, não é recomendado a execução do mesmo, pois pode
apresentar alguma mensagem de erro por conta da forma de apresentação
"""
#

#########               Funções                ##############
"""
Funções são blocos de código com um único objetivo e que necessitam ser execultadas 
diversas vezes. Um exemplo é uma função que some dois números a e b. Para que não 
seja escrito diversas vezes a mesma coisa, é utilizado uma função.

Algumas fuções próprias do python já vem pré definidas na linguagem, como: print, input,
sum, min, max e tantas outras.

** Funções padrões do python: https://docs.python.org/pt-br/3/library/functions.html

Uma função é definida por:
def nome_da_função(parametros):
    bloco de código
    return x

def -> parametro que define uma função, ou seja, o tipo que aquele bloco de dados se refere.
nome_da_função -> nome pela qual a função será chamada, possui as mesmas limitações de nome de 
                váriavel (descrita no item 1). Por padrão, a comunidade python utiliza texto em
                minúsculo para nome de funções.
bloco de código -> O que a função irá fazer.
return x -> retorna o valor de x. Exemplo é o imput que retorna o valor que o se é digitado.
            Sua aplicação no código não é obrigatoria, tudo dependerá do modo de aplicação.

Exemplos:
"""
def somador(a,b):
    return a+b

def somador2(a,b):
    print(a+b)

def eh_primo(x):
    cont = 1
    for i in range(x):
        if cont%i == 0:
            cont += 1
    print("É primo")

def printar_random():
    import random
    print(random.randint(0,100))

def return_random():
    import random
    return random.randint(0,100)

"""
Para chamar uma função, basta chamar seu nome e seus parametros entre parenteses, se considerarmos
os exemplos a cima, basta fazer: somador(a,b) e a soma será retornado.
O valor do retorno pode ser armazenada em uma variavel ou utilizada em outra coisa. Exemplos:
"""
soma = somador(1,2)
print(somador(3,5))
soma2 = somador(return_random,return_random)
eh_primo(5416463486467)


#########               Recursividade                ##############
"""
A recursividade é um modo da função chamar a si mesma, ou seja, dentro do bloco de programação
a função chamara ela até que se atinja uma condição de parada.
Um exemplo clássico pe o de Fibonacci:
"""
def fibonacci(n):
    if n < 0:
        print("Valor Incorreto!")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

"""
Ao chamar fibonacci(5), será feito a chamada da função até que o valor de parada seja atingido.
Ou seja...
n == 5 vai entrar no else e irá charmar fibonacci(4) + fibonacci(3)
n == 4, irá charmar fibonacci(3) + fibonacci(2)
n == 3, irá charmar fibonacci(2) + fibonacci(1)
Com isso, chegara em  elif n == 1 or n == 2, e será retornado o valor 1 e em seguida será somado
com os valores a cima.

Para melhor entendimento, aqui vai uma explicação básica.
Sempre que uma função é chamada, o código a baixo dela só será execultado após o retorno daquele valor.
Exemplo:
for i in range(10):
    print(fibonacci(i))
assim que a função fibonacci é chamada, o for é congelado até que a função retorne um valor e o print 
imprima.

Com a recursividade acontece o mesmo. A função vai sendo chamadas n vezes até atingir a condição de parada.
ou seja...
fibonacci                               | 
    fibonacci                           |
        fibonacci                       | A função vai descendo enquanto é chamada e dando "pausa"nas outras.
            fibonacci                   |
                fibonacci               |
                    fibonacci           V

Quanto se é atingido o caso de parada o valor sai retornando.
fibonacci                               ^ 
    fibonacci                           |
        fibonacci                       | E assim por diante... até chegar na primeira chamada da função
            fibonacci                   | Retorna (x+x) + x
                fibonacci               | Retorna x + x
                    fibonacci           | Retorna x

"""