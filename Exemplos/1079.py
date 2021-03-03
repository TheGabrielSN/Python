# https://www.urionlinejudge.com.br/judge/pt/problems/view/1079

x=(int(input()))
for s in range(x):
    n1,n2,n3=map(float,input().split())
    m=((n1*2)+(n2*3)+(n3*5))/(10)
    print("{:.1f}".format(m))
