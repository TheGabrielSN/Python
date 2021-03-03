# https://www.urionlinejudge.com.br/judge/pt/problems/view/1061

v1=input().split()
d1=int(v1[1])
v2=input().split(" : ")
h1,m1,s1=list(map(int,v2))
v1=input().split()
d2=int(v1[1])
v2=input().split(" : ")
h2,m2,s2=list(map(int,v2))
d=d2-d1
h=h2-h1
m=m2-m1
s=s2-s1
if m>=1 or h>=1 or d>=1:
    if h<0:
        h=24+h
        d=d-1
    if m<0:
        m=60+m
        h=h-1
    if s<0:
        s=60+s
        m=m-1
    if d<=0:
        d=0
    print("{} dia(s)".format(d))
    print("{} hora(s)".format(h))
    print("{} minuto(s)".format(m))
    print("{} segundo(s)".format(s))
