# https://www.urionlinejudge.com.br/judge/pt/problems/view/1159

while True:
    x=int(input())
    if x==0:
        break
    if x%2==1:
        x+=1
    soma=int(0)
    c=5
    while c>0:
        soma+=x
        x+=2
        c-=1
    print(soma)
    
