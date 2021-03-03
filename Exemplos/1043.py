# https://www.urionlinejudge.com.br/judge/pt/problems/view/1043

A,B,C=map(float,input().split())
s=float(0)
if A+B>C and B+C>A and A+C>B:
    s=A+B+C
    print("Perimetro = {:.1f}".format(s))
else:
    s=(0.5*(A+B)*C)
    print("Area = {:.1f}".format(s))