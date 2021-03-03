# https://www.urionlinejudge.com.br/judge/pt/problems/view/1435

while True:
    x=int(input())
    if x==0:
        break
    matriz=[]
    for l in range(x):
        matriz.append([])
        for c in range(x):
            matriz[l].append(1)
    atual=1
    cima=0
    esquerda=0
    baixo=x-1
    direita=x-1
    if x%2==0:
      meio=x/2
    if x%2==1:
      meio=(x+1)/2
    while atual<=meio:
      i=esquerda
      while i<=direita:
        matriz[cima][i]=atual
        matriz[baixo][i]=atual
        i+=1
      i=cima+1
      while (i<baixo):
          matriz[i][esquerda]=atual
          matriz[i][direita]=atual
          i+=1
      atual+=1
      cima+=1
      baixo-=1
      esquerda+=1
      direita-=1
    for l in range(x):
        for c in range(x):
            if c==x:
                print(" ",matriz[l][c],end="\n")
            elif c==0 and l!=0:
                print("\n ",matriz[l][c],end="")
            elif c==0 and l==0:
                print(" ",matriz[l][c],end="")
            else:
                print("%4d"% matriz[l][c],end="")
    print("\n")
