# https://www.urionlinejudge.com.br/judge/pt/problems/view/1064

s=0
m=0
for i in range(6):
    n1=float(input())
    if n1>0:
        s+=1
        m+=n1
        s2=m/s
print("{} valores positivos".format(s))
print("{:.1f}".format(s2))
