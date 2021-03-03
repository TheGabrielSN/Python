# https://www.urionlinejudge.com.br/judge/pt/problems/view/2968

a,b=map(int,input().split())
total=a*b
lista=[]
for i in range(10,100,10):
    s=i/100*total
    if int(s)<s:
        s+=1
    lista.append(int(s))
for i in range(9):
    if i!=8:
        print(lista[i], end=" ")
    else:
        print(lista[i])
