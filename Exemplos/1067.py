# https://www.urionlinejudge.com.br/judge/pt/problems/view/1067

x=int(input())
if x%2==0:
    for s in range(1,x,2):
        print(s)
else:
    for s in range (1,x+1,2):
        print(s)
