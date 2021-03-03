# https://www.urionlinejudge.com.br/judge/pt/problems/view/1133

x=int(input())
y=int(input())
if x>=y:
    for i in range(y+1,x):
        if i%5==2 or i%5==3:
            print(i)            
if y>x:
    for i in range(x+1,y):
        if i%5==2 or i%5==3:
            print(i)
