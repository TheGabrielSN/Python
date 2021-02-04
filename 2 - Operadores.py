#
"""
Obs: Arquivo apenas informacional, não é recomendado a execução do mesmo, pois pode
apresentar alguma mensagem de erro por conta da forma de apresentação
"""
#

#########               Operadore                ##############
"""
Divididos entre lógicos, aritméticos e relacionais, os operadores são utilizados para diversas
funcionabilidades dentro de um código, indo desde facilitar a escrita até funções
importantes para o desenvolvimento do código.

Cada operador possui uma ordem de prioridade e quanto menor for, maior é
sua importancia, ou seja, os operadores são executados de acordo sua prioridade,
indo do menor para o maior.
"""

#########               Aritméticos                ##############
"""
> atribuição       '='  prioridade - 10 : serve para atribuir um dado a uma váriavel
> parênteses       '()' prioridade - 1 : utilizado para dar prioridade a alguma expressão
> elevado          '**' prioridade - 2 : utilzado para para fazer a exponenciação de um número 
                                          (3**2 "três elevado ao quadrado")
> positivo         '+'  prioridade - 3 : utilzado para denominar um número positivo, pouco usado,
                                          pois qualquer número sem o negatico é denomindado positivo
> negativo         '-'  prioridade - 3 : utilzado para denominar um número negativo
> multiplicação    '*'  prioridade - 4 : utilizado para multiplicar dois número
> divisão          '/'  prioridade - 4 : utilizado para dividir dois números
> divisão exata    '//' prioridade - 4 : utilizado para dividir dois números sem que exista casas decimais
> resto da divisão '%'  prioridade - 4 : utilizado para pegar o resto de uma divisão inteira
> soma             '+'  prioridade - 5 : utilizado para somar dois números
> subtração        '-'  prioridade - 5 : utilizado para subtrair dois números

exemplos:
(1+2)*3  ->  9
2**3     ->  8
+15
-(5+3)   -> -8
5*3      -> 15
5/3      -> 1,66
5//3     -> 1
5%3      -> 2
5+3      -> 8
5-3      -> 2
"""

#########               Relacionais                ##############
"""
O resultado de cada operador relacional é dado em True (quando a comparação é verdadeira)
e False (quando a comparação é falsa).
> menor que      '<'  prioridade - 6 : "
> menor ou igual '<=' prioridade - 6 : "
> maior que      '>'  prioridade - 6 : "
> maior ou igual '>=' prioridade - 6 : "
Os operadores acima são utilizados para compara dois valores (normalmente, números).

> igualdade      '==' prioridade - 6 : Compara se dois valores são iguais
> diferença      '!=' prioridade - 6 : Compara se dois valoes são diferentes
Esses dois operadores são comumente utilizados para comparar qualquer tipo de dado.

exemplos:
5 < 3  -> False
5 <= 3 -> False
5 > 3  -> True
5 >= 3 -> True
5 == 3 -> False
5 != 3 -> True
"""

#########               Logicos                ##############
""" 
> not prioridade - 7 : utilizado para inverter qualquer condição
                       (se for False, se torna True. se for True, se torna False)
> and prioridade - 8 : utilizado para verifivar de duas ou mais condições são verdadeiras.
                       (caso as duas condições sejam verdadeiras, o and retorna True.
                        caso qualquer condução seja false, o and retorna False.)
> or  prioridade - 9 : utilzado para verificar se alguma condição é verdadeira.
                       (caso qualquer condição entre os 'or' for verdadeira, é retornado True)
exemplos:
not True       -> False
True and False -> False
True or False  -> True
"""