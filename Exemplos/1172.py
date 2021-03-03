# https://www.urionlinejudge.com.br/judge/pt/problems/view/1172

lista=[]
for i in range(10):
    x=int(input())
    if x<=0:
        lista.append(1)
    else:
        lista.append(x)
    print("X[{}] = {}".format(i,lista[i]))
