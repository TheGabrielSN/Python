# https://www.urionlinejudge.com.br/judge/pt/problems/view/1145

x,y=map(int,input().split())
c=1
for i in range(1,int((y/x))+1):
    r=""
    for s in range(x):
        r+=str(c)+" "
        c+=1
    print(r[:-1])
