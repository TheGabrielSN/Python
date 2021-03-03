# https://www.urionlinejudge.com.br/judge/pt/problems/view/2963

n=int(input())
lista=[]
for i in range(n):
    lista.append(int(input()))
if lista[0]==max(lista):
    print("S")
else:
    print("N")
