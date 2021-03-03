# https://www.urionlinejudge.com.br/judge/pt/problems/view/1099

n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    s=0
    if x>y:
        t=x
        x=y
        y=t
    if x%2!=0:
        x+=2
        while x<y:
            if x%2!=0:
                s+=x
            x+=1
    else:
        x+=1
        while x<y:
            if x%2!=0:
                s+=x
            x+=1
    print(s)
