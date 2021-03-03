# https://www.urionlinejudge.com.br/judge/pt/problems/view/1038

A,B=map(float,input().split())
Y1=4.00
Y2=4.50
Y3=5.00
Y4=2.00
Y5=1.50
X1=B*Y1
X2=B*Y2
X3=B*Y3
X4=B*Y4
X5=B*Y5
if A==1:
    print('Total: R$ {:.2f}'.format(X1))
if A==2:
    print('Total: R$ {:.2f}'.format(X2))
if A==3:
    print('Total: R$ {:.2f}'.format(X3))
if A==4:
    print('Total: R$ {:.2f}'.format(X4))
if A==5:
    print('Total: R$ {:.2f}'.format(X5))