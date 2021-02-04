#
"""
Obs: Arquivo apenas informacional, não é recomendado a execução do mesmo, pois pode
apresentar alguma mensagem de erro por conta da forma de apresentação
"""
#

#########               if                ##############
"""
Traduzido do inglês, if significa "se" e é utilizado para criar uma condição dentro do
código.
O if é executado quando uma condição se torna verdadeira.
maneira de escrita:
    if(True):, onde:
        tudo que estiver dentro do () precisa ser veridadeiro para que o bloco de 
        instruções abaixo seja executado.
    exemplo:
        a = 10
        if(a == 10):
            print("O número é 10")
        --------------------------------
        No caso desse exemplo, o print só será executado caso a condição dentro do () seja
        verdadeiro, ou seja, a for igual a 10. Caso a condição não seja verdadeira, o codigo
        dentro do if é ignorado e segue-se com a execução do programa.      
"""
x = 9
if(x%2 == 0):
    print("O número é par")

#########               else                ##############
"""
Traduzido do inglês, else significa "se não" e é utilizado para criar uma forma de executar um
bloco de código caso a condição no if seja realizado.
O else só pode ser utilizado depois do if.
exemplo:
    a = 10
    if(a%2 == 0):
        print("O número é par")
    else:
        print("O número é ímpar")
    ---------------------------------
    Nesse exemplo, se o número representado por a for par, ele executa o if (O número é par),
    se o número for impar, ele executa o else (O número é ímpar)
"""
a = 25
if(a%2 == 0):
    print("O número é par")
else:
    print("O número é ímpar")

#########               elif                ##############
"""
elif é literalmente a junção entre else e if, utilizado para criar um outro bloco de execução.
Assim como o else, só pode ser executado depois de um if.
podendo ser escrito como else if ou elif, funciona como um nova condição para um bloco de códigos.
exemplo:
    a = 0                                                   a = 0
    if(a%2 == 0):                                           if(a%2 == 0):
        print("O número é par")                                 print("O número é par")
    elif(a == 0):                                           else if(a == 0):
        print("O número é nulo")                                print("O número é nulo")
    else:                                                   else:
        print("O número é ímpar")                               print("O número é ímpar")
    Os dois códigos funcinam do mesmo jeito, a unica diferença é a escrita.
"""
a = 0
if(a%2 == 0):
    print("O número é par")
elif(a == 0):
    print("O número é nulo")
else:
    print("O número é ímpar") 

#########               "Cascata" de decisão                ##############
"""
É possivel fazer a implementação de quantos if ou elif forem necessarios de modo seguido.
O unico obrigatorio a ser colocado é o if, o elif ou o else são opcionais dependendo da 
funcionabilidade do código no geral.

exemplo:
    a = int(input())
    if(a == 0):
        ...
    elif(a == 1):
        ...
    elif(a == 2):
        ...
    elif(a == 3):
        ...
    elif(a == 4):
        ...
    elif(a == 5):
        ...
    elif(a == 6):
        ...
    elif(a == 7):
        ...
    elif(a == 8):
        ...

------------------------------------------------
Diferença entre sequencias de if e sequencias de elif:
    Em uma sequencia de if's:
        if(...):
            ...
        if(...):
            ...
        if(...):
            ...
        if(...):
            ...
    A condição de um if pode acabar entrando em outro if, ou seja
    pode acontecer de que todos os if's sejam executados, dependendo
    de cada condição.

    Em uma sequencia de elif's:
        if(...):
            ...
        elif(...):
            ...
        elif(...):
            ...
        elif(...):
            ...
    Na questão dos elif's, cada elif só será executado cado o if/elif
    anterior for false, ou seja, só sera executado um bloco de código entre
    eles.
"""