# https://www.urionlinejudge.com.br/judge/pt/problems/view/1176

e=int(input())
for I in range(e):
    x=int(input())
    ant=0
    atu=1
    s=[]
    for i in range(x+1):
        s.append(ant)
        t=ant
        ant=atu
        atu=atu+t
    print("Fib({}) = {}".format(x,s[x]))
