# https://www.urionlinejudge.com.br/judge/pt/problems/view/1015

import math
A,B=map(float, input().split())
C,D=map(float, input().split())
X=math.sqrt(((C-A)**2) + ((B-D)**2)) 
print('{:.4f}'.format(X))