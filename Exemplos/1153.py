# https://www.urionlinejudge.com.br/judge/pt/problems/view/1153

x=int(input())
c,n=x-1,x
while c>0:
    n=n*c
    c-=1
print(n)
