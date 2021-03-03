# https://www.urionlinejudge.com.br/judge/pt/problems/view/1020

A = int(input())
X1 = int(A / 365)
X2 = int((A%365/30))
X3= int(A%365%30)

print('{} ano(s)\n{} mes(es)\n{} dia(s)'.format(X1,X2,X3))