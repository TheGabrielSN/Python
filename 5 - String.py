#
"""
Obs: Arquivo apenas informacional, não é recomendado a execução do mesmo, pois pode
apresentar alguma mensagem de erro por conta da forma de apresentação
"""
#

"""
> Link de referencia do material: https://algoritmosempython.com.br/cursos/programacao-python/strings/ <
"""
#########               Definição                ##############
"""
String, em português palavra, representa qualquer tipo de texto a ser utilizado 
dentro do programa.

Em python, toda string é representada por um texto entre ' '(aspas simples)/" "(aspas duplas)
/""" """ e ''' '''(tripla aspas duplas ou simples)

A utilização de cada um depende do desejo do programador, mas, por convenção entre os programadores
python, ' ' é utilizado para definir texto que faz parte de um comando ou apenas uma letra,
" " é utilizado para definir
o texto que será utilizado, """ """ é utilizado para duas funções: a primeira é criar um texto de
multiplas linhas e a segunda é para descrever o funcionamento de uma classe.
"""

texto1 = 'a'
texto2 = "Texto a ser apresentado"
texto3 = """Esse texto
            Possui multipals
            linhas"""

#########               Metodos                ##############
"""
-> len() serve para contar a quantidade de letras do texto, exemplo: len("texto") o resultado é 5
--> codigo:
    texto = input()
    NumeroLetras = len(texto)
    print("Número de letras da string: {}".format(NumeroLetras))

-> capitalize() serve para formatar a string de acordo com o padrão capitalize
--> codigo:
    texto = "texto aleatorio"
    print(texto.capitalize())
A saída será: Texto Aleatorio

-> isdigit() verifica se o texto possui apenas números
--> codigo:
    texto = "12345"
    print(texto.isdigit())
A saída será True, pois o texto possue apenas número.

-> isalnum() (isalnum - Is Alfa Numeric) verifica se o texto possui numeros e letras
--> codigo:
    texto = "abc123"
    printf(texto.isalnum())
A saída será True, pois o texto possue letra e número.
"""

#########               Slicing                ##############
"""
Definição: Slicing é uma operação para modificar a string, pegando apenas parte da mesma.
Uma strign por ser acessada por posição. Exemplo:

                     P  y  t  h  o  n
                     0  1  2  3  4  5
                    -6 -5 -4 -3 -2 -1

A primeira letra da string é representado por 0, após isso se tem uma sequência de posições.
Também temos uma ordem inversa, onde o final da strinf começa com -1 e vem diminuindo até chegar
ao inicio da string. Para acessar cada posição, é necessario colocar a string em uma variavel e 
depois passar a posição entre []
Exemplo:
    texto = "Python"
    texto[0] -> ao fazer isso, estamos acessando a string na posição 0, que representa o P
    texto[1] -> representa o y
    texto[-1] -> representa o n

Na tradução slicing é cortar, e para isso usamos um padrão com a posição de inicio e fim do slicing.
Exemplo:
    texto[2:4] -> a saída será th, pois esse corte se ínicia no 2 e termina no 4, mas n pega a ultima
    posição. Se compararmos com matemática, diriamos que [2:4] é [2, 4) (fechado no 2 e aberto no 4).
    texto[1:5:2] -> começa no 1, termina no 5 e vai de 2 em 2, ou seja, a saída será: yh
    texto[::-1] -> a saída será: nohtyP, ou seja, inverteu a string, isso se da pelo seguinte motivo:
    [(inicio):(fim):(pulo)], caso inicio não seja dito, ele começa no inicio da string, o fim acontece
    o mesmo.
    [(inicio):(fim):(pulo)] Ao fazer isso, precisamos definir ao menos um parameto, enquanto o python
    irá fazer a substituição dos outros itens.
    > [(inicio)] -> fim é definido como inicio+1 (proxima posição) e pulo é definido como 1, resultando
    na obtenção de apenas uma letra
    >[:(fim)] -> inicio é definido como o inicio da string, pulo é definido como 1, resultando na
    obtenção de parte da string indo até o fim.
"""

#########               Operações                ##############
"""
String só possue dois tipos de operações:
+  -> onde uma string será concatenada com a outra
    > Funciona apenas com string + string
Exemplo:
    "Python" + " " + "Programação"
    O resultado é: "Python Programação"

*  -> é feita a reperição de uma string.
    > Funciona apenas com string * int
Exemplo:
    "Python"*3
    O resultado é: "PythonPythonPython"
"""

#########               String e variavel                ##############
"""
Os metodos apresentados na parte de print na introdução,(como: f"{variavel} texto", 
"{} texto".format(variavel), etc)
funcionam para a manipulação de strings também.
Exemplo:
    nome = "Aleatorio"
    f"Olá {nome}"
    O resultado é: "Olá Aleatorio"
"""