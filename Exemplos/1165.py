# https://www.urionlinejudge.com.br/judge/pt/problems/view/1165

x=int(input())
for i in range(x):
    n=int(input())
    c=0
    for I in range(1,n+1):
        if n%I==0 or n%I==n:
            c+=1
    if c==2:
        print("{} eh primo".format(n))
    else:
        print("{} nao eh primo".format(n))
