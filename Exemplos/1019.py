# https://www.urionlinejudge.com.br/judge/pt/problems/view/1019

A=int(input())
X1=int(A/60/60)
X2=int((A/60)-(X1*60))
X3=int(A-((X1*60*60)+(X2*60)))
print(str(X1)+':'+str(X2)+':'+str(X3))