# https://www.urionlinejudge.com.br/judge/pt/problems/view/2003

while True:
    try:
        x,y = map(int, input().split(':'))
        if x>=7:
            y += (x-7)*60
        else:
            y = 0
        print("Atraso maximo: {}".format(y))
    except EOFError:
        break
