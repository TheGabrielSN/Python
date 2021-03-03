# https://www.urionlinejudge.com.br/judge/pt/problems/view/1070

x=int(input())
if x%2==0:
    for s in range(x+1,x+12,2):
        print(s)
if x%2==1:
    for s in range(x,x+12,2):
        print(s)
