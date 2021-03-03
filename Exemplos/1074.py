# https://www.urionlinejudge.com.br/judge/pt/problems/view/1074

x=int(input())
for i in range(x):
    n=int(input())
    if n==0:
        print("NULL")
    if n>0 and n%2==0:
        print("EVEN POSITIVE")
    if n<0 and n%2==0:
        print("EVEN NEGATIVE")
    if n>0 and n%2==1:
        print("ODD POSITIVE")
    if n<0 and n%2==1:
        print("ODD NEGATIVE")
