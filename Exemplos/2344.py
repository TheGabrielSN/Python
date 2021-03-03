# https://www.urionlinejudge.com.br/judge/pt/problems/view/2344

x=int(input())
if(x==0):
    print("E")
if(x>=1 and x<=35):
    print("D")
if(x>=36 and x<=60):
    print("C")
if(x>=61 and x<=84):
    print("B")
if(x>=86 and x<=100):
    print("A")