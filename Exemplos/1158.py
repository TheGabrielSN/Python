# https://www.urionlinejudge.com.br/judge/pt/problems/view/1158

e=int(input())
soma=int(0)
for i in range(e):
    x,y=map(int,input().split())
    if x%2==0:
        x+=1
    while y>0:
        soma+=x
        y-=1
        x+=2
    print(soma)
    soma=int(0)
