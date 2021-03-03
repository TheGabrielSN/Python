# https://www.urionlinejudge.com.br/judge/pt/problems/view/1175

lista=[]
listaIn=[]
for i in range(20):
    x=int(input())
    lista.append(x)
for I in range(len(lista)-1,-1,-1):
    listaIn.append(lista[I])
for s in range(len(listaIn)):
    print("N[{}] = {}".format(s,listaIn[s]))
