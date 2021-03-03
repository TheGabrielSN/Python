# https://www.urionlinejudge.com.br/judge/pt/problems/view/1146

x=int(input())
s=""
while True:
    for i in range(1,x+1):
        if x!=i:
            s+=str(i)+" "
        if x==i:
            s+=str(i)
    print(s)
    s=""
    x=int(input())
    if x==0:
        break
