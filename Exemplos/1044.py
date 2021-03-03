# https://www.urionlinejudge.com.br/judge/pt/problems/view/1044

n1,n2=map(int,input().split())
if n1%n2==0 or n2%n1==0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")