# https://www.urionlinejudge.com.br/judge/pt/problems/view/1060

s=0
for i in range(6):
    n1=float(input())
    if n1>0:
        s+=1
print("{} valores positivos".format(s))