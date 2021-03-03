# https://www.urionlinejudge.com.br/judge/pt/problems/view/1173

lista=[]
x=int(input())
c=x
lista.append(x)
for i in range(10):
    print("N[{}] = {}".format(i,lista[i]))
    c=c*2
    lista.append(c)
