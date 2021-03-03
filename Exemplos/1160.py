# https://www.urionlinejudge.com.br/judge/pt/problems/view/1160

x=int(input())
for i in range(x):
    c1=float(0)
    c2=float(0)
    a,b,cp1,cp2=map(float,input().split())
    ano=0
    while True:
        c1=int((cp1/100)*a)
        c2=int((cp2/100)*b)
        ano+=1
        a+=c1
        b+=c2
        if a>b or ano>101:
            break
    if ano>100:
        print("Mais de 1 seculo.")
    else:
        print("{} anos.".format(ano))