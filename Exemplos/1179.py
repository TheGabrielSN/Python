# https://www.urionlinejudge.com.br/judge/pt/problems/view/1179

par=[]
impar=[]
for I in range(15):
    if len(par)==5:
        for i in range(len(par)):
            print("par[{}] = {}".format(i,par[i]))
        par=[]
    if len(impar)==5:
        for i in range(len(impar)):
            print("impar[{}] = {}".format(i,impar[i]))
        impar=[]
    x=int(input())
    if x%2==0:
        par.append(x)
    if x%2==1:
        impar.append(x)
for i in range(len(impar)):
    print("impar[{}] = {}".format(i,impar[i]))
for i in range(len(par)):
    print("par[{}] = {}".format(i,par[i]))
