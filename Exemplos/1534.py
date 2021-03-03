# https://www.urionlinejudge.com.br/judge/pt/problems/view/1534

while True:
    try:
        x=int(input())
        matriz=[]
        C=x-1
        L=0
        for l in range(x):
            matriz.append([])
            for c in range(x):
                if l==L and c==C:
                    matriz[l].append(2)
                elif c==l:
                    matriz[l].append(1)
                else:
                    matriz[l].append(3)
            C-=1
            L+=1
        for l in range(x):
            for c in range(x):
                print(matriz[l][c], end="")
            print("")
    except EOFError:
        break
