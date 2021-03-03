# https://www.urionlinejudge.com.br/judge/pt/problems/view/1035

A,B,C,D = map(int,input().split())
X1=A+B
X2=C+D
X3=A%2
if B>C and D>A and X2>X1 and C>0 and D>0 and X3==0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')