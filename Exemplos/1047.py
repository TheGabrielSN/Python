# https://www.urionlinejudge.com.br/judge/pt/problems/view/1047

h1,m1,h2,m2=map(int,input().split())
i=h1*60+m1
f=h2*60+m2
d=0
if h1<=h2:
    d=f-i
    if d==0:
       print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)"%(24,d%60))
    else:
        print("O JOGO DUROU {:.0f} HORA(S) E {:.0f} MINUTO(S)".format((d-d%60)/60,d%60))
else:
    d=(24*60-i)+f
    print("O JOGO DUROU {:.0f} HORA(S) E {:.0f} MINUTO(S)".format((d-d%60)/60,d%60))