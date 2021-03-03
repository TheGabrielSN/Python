#
"""
Obs: Arquivo apenas informacional, não é recomendado a execução do mesmo, pois pode
apresentar alguma mensagem de erro por conta da forma de apresentação
"""
#

https://docs.python.org/pt-br/3/tutorial/datastructures.html

#########               Definição                ##############
"""
Listas em python é nada mais que uma estrutura de dado, onde pode se organizar qualquer tipo de dado
em uma lista.

a lista é definida como o tipo list.

A lista é definina com [], e seus dados podem ser de qualquer tipo, separados por virgula.
Exemplo:
    Lista = [] -> Lista vazia
    numeros = [0,1,2,3,4,5,6,7,8,9]
    vogais = ["a","e","i","o","u"]
    lista = ["a", 0, 5.3, False]

Seu tamanho é indefinido, limitando-se a memoria do dispositivo ao qual está sendo execultado o programa.
"""

#########               Metodos                ##############
"""
-> append(x) - adiciona o elemento x no fim da lista
->código:
	lista=[]
	lista.append(1) # lista é igual a [1]
	lista.append(2) # lista é igual a [1,2]

-> extend(lista2) - adiciona todos os elementos da lista2 ao final da lista principal
-> código:
	lista = [1,2,3,4,5]
	lista2 = [6,7,8,9]
	lista.extend(lista2) # lista é igual a [1,2,3,4,5,6,7,8,9]

-> insert(i,x) adiciona o valor x na posição de i
-> código:
	lista = []
	lista.insert(0,10) # lista é igual a [10]
	lista.insert(0,58) # lista é igual a [58,10]
	lista.insert(2,58) # lista é igual a [58,10,58]
	
-> remove(x) - remove o primeiro elemento igual a x
-> código:
	lista=[0,2,4,6,8,9,5,9]
	lista.remove(9) # lista é igual a [0,2,4,6,8,5,9]
	
-> pop([i]) - remove o elemento de acordo com o i
-> código:
	lista = [0,2,4,6,8]
	lista.pop([5]) # lista é igual a [0,2,4,6]

-> clear() - remove todos os elementos da lista
-> código:
	lista=[1,2,3,4,5]
	lista.clear() # lista é igual a []
	
-> count(x) - conta quantas vezes x aparece na lista
-> código:
	lista=[1,2,2,3,4,5,5,5]
	lista.cout(4) # retorna o valor 1
	lista.cout(5) # retorna o valor 3
	
-> sort() - ordena a lista de forma crescente
-> códigos:
	lista=[0,2,1,3,6,5]
	lista.sort() # a lista é igual a [0,1,2,3,5,6]
	
-> reverse() - inverte os valores da lista
-> código:
	lista=[0,2,5,8]
	lista.reverse() # a lista é igual a [8,5,2,0]
	

"""