# https://www.urionlinejudge.com.br/judge/pt/problems/view/3140

controle = 0
while True:
    try:
        n = input()

        if n == '':
            break
        if n == "    <body>":
            controle = 1
        if n == "    </body>":
            controle = 0
        if controle == 1 and n != "    <body>":
            print(n)
    except EOFError:
        break