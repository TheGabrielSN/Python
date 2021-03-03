# https://www.urionlinejudge.com.br/judge/pt/problems/view/1036

import math 
A,B,C = map(float,input().split())
X1=0
X2=0
X3=(B**2)-(4*A*C)
if X3<0 or A==0:
    print('Impossivel calcular')
else:
    X3=math.sqrt(X3)
    X1=(-B+X3)/(2*A)
    X2=(-B-X3)/(2*A)
    print('R1 = {:.5f}\nR2 = {:.5f}'.format(X1,X2))