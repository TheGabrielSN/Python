# https://www.urionlinejudge.com.br/judge/pt/problems/view/1013

import math
A,B,C=input().split()
X=(int(A) + int(B) + abs(int(A) - int(B)))  / 2
X1=(int(X) + int(C) + abs(int(X) - int(C)))/2
print('{:.0f} eh o maior'.format(X1))