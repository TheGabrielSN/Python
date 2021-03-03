# https://www.urionlinejudge.com.br/judge/pt/problems/view/1478

while True:
    N = int(input())
    if (N == 0):
        break
    resultado =  []
    for a in range(1,(N+1)):
        lista = []
        count = a
        for b in range(N):
            lista.append(abs(count))
            if(count == 1):
                count -= 3
            else:
                count -= 1
        resultado.append(lista)
    for a in range(N):
        tx = ''
        for b in range(N):
            tx += " %3d" %resultado[a][b]
        print(tx[1:])
    print("")