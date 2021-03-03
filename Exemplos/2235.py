# https://www.urionlinejudge.com.br/judge/pt/problems/view/2235

a,b,c = map(int, input().split())
soma = a+b+c
if (a==b) or (a==c) or (b==c):
    print("S")
elif(soma == a*2) or (soma == b*2) or (soma == c*2):
    print("S")
else:
    print("N")