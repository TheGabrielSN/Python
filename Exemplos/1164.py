# https://www.urionlinejudge.com.br/judge/pt/problems/view/1164

x=int(input())
for i in range(x):
    n=int(input())
    soma=0
    for I in range(1,n+1):
        if n%I==0 and I!=n:
            soma+=I
    if soma==n:
        print("{} eh perfeito".format(n))
    else:
        print("{} nao eh perfeito".format(n))
