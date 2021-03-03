# https://www.urionlinejudge.com.br/judge/pt/problems/view/1174

lista=[]
for i in range(100):
    x=float(input())
    lista.append(x)
for I in range(100):
    if lista[I]<=10:
        print("A[{}] = {}".format(I,lista[I]))
