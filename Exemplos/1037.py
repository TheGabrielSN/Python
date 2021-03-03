# https://www.urionlinejudge.com.br/judge/pt/problems/view/1037

A=float(input())
if A<0 or A>100:
    print('Fora de intervalo')
elif A>=0 and A<=25:
    print('Intervalo [0,25]')
elif A>=25 and A<=50:
    print('Intervalo (25,50]')
elif A>=50 and A<=75:
    print('Intervalo (50,75]')
elif A>=75 and A<=100:
    print('Intervalo (75,100]')
