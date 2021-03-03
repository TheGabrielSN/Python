# https://www.urionlinejudge.com.br/judge/pt/problems/view/1101

x,y=1,1
r=""
su="Sum="
se=1
soma=int(0)
while True:
    x,y=map(int,input().split())
    if x<=0 or y<=0:
        break
    if x>=y:
        for s in range(y,x+1):
            if se==1:
                r=r+str(s)
                soma+=s
                se+=1
            else:
                r=r+" "+str(s)
                soma+=s
                se+=1
        su=su+str(soma)
        r=r+" "+su
        print(r)
    if y>x:
        for s in range(x,y+1):
            if se==1:
                r=r+str(s)
                soma+=s
                se+=1
            else:
                r=r+" "+str(s)
                soma+=s
                se+=1
        su=su+str(soma)
        r=r+" "+su
        print(r)
    r=""
    su="Sum="
    se=1
    soma=int(0)
