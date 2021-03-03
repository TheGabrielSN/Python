# https://www.urionlinejudge.com.br/judge/pt/problems/view/1151

x=int(input())
ant=0
atu=1
s=""
for i in range(x):
    if i==x-1:
        s+=str(ant)
    else:
        s+=str(ant)+" "
    t=ant
    ant=atu
    atu=atu+t
print(s)
