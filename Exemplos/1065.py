# https://www.urionlinejudge.com.br/judge/pt/problems/view/1065

s=0
for i in range(5):
    n1=float(input())
    if n1%2==0:
        s+=1
print("{} valores pares".format(s))
