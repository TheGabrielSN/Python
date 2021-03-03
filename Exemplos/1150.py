# https://www.urionlinejudge.com.br/judge/pt/problems/view/1150

x=int(input())
z=int(input())
soma=x
c=1
while True:
    if x>=z:
        z=int(input())
    else:
        break
while soma<z:
    soma=soma+(x+1)
    c+=1
    x+=1
print(c)
