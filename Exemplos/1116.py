# https://www.urionlinejudge.com.br/judge/pt/problems/view/1116

x=int(input())
s=float(0)
for i in range(x):
    x,y=map(int,input().split())
    if y==0:
        print("divisao impossivel")
    else:
        s=float(x/y)
        print(s)
