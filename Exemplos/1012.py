# https://www.urionlinejudge.com.br/judge/pt/problems/view/1012

A,B,C = map(float, input().split())
D=3.14159
X1=A*C/2
X2=D*C**2
X3=(A+B)*C/2
X4=B**2
X5=A*B
print('TRIANGULO: {:.3f}'.format(X1))
print('CIRCULO: {:.3f}'.format(X2))
print('TRAPEZIO: {:.3f}'.format(X3))
print('QUADRADO: {:.3f}'.format(X4))
print('RETANGULO: {:.3f}'.format(X5))