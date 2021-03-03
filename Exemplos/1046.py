# https://www.urionlinejudge.com.br/judge/pt/problems/view/1046

h1,h2=map(int,input().split())
s1=(24-h1)+h2
s2=h2-h1
if s1<=24 or s2<=24:
    if h1==h2:
       print("O JOGO DUROU 24 HORA(S)")
    else:
        if h1>h2:
            print("O JOGO DUROU {} HORA(S)".format(s1))
        if h2>h1:
            print("O JOGO DUROU {} HORA(S)".format(s2))