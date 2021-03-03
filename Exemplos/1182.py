# https://www.urionlinejudge.com.br/judge/pt/problems/view/1182

coluna=int(input())
oper=str(input())
soma=int(0)
for l in range(12):
    for c in range(12):
        v=float(input())
        if coluna == c:
            soma+=v
if oper=="S":
    print("{:.1f}".format(soma))
if oper=="M":
    print("{:.1f}".format(float(soma/12)))
