# https://www.urionlinejudge.com.br/judge/pt/problems/view/1045

A,B,C=map(float,input().split())
a=A
b=B
c=C
if A>0 and B>0 and C>0:
    if A!=B:
        if A<B:
            a=B
            b=A
    if A!=C:
        if a<C:
            c=B
            a=C
    if C!=B:
        if C>B:
            c=A
            b=B
    if a>=b+c:
        print("NAO FORMA TRIANGULO")
    else:
        if (a**2)==((b**2)+(c**2)):
            print("TRIANGULO RETANGULO")
        if (a**2)>((b**2)+(c**2)):
            print("TRIANGULO OBTUSANGULO")
        if (a**2)<((b**2)+(c**2)):
            print("TRIANGULO ACUTANGULO")
        if a==b==c:
            print("TRIANGULO EQUILATERO")
        else:
            if a==b or a==c or b==c:
                print("TRIANGULO ISOSCELES")
