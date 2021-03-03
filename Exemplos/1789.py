# https://www.urionlinejudge.com.br/judge/pt/problems/view/1789

while True:
    try:
        x=int(input())
        lista=[]
        a=map(int,input().split())
        for i in a:
            lista.append(i)
        cont=0
        maior=0
        for i in range(x):
            if lista[i]>maior:
                maior=lista[i]
            if maior<10:
                cont=1
            if maior>=10 and maior<20:
                cont=2
            if maior>=20:
                cont=3
        print(cont)
    except:
        break
