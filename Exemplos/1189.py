# https://www.urionlinejudge.com.br/judge/pt/problems/view/1189

matriz=[]
oper=str(input())
x=int(0)
for l in range(12):
    matriz.append([])
    for c in range(12):
        matriz[l].append(float(input()))
if oper=="S":
    for l in range(12):
        for c in range(12):
            if l>c and l+c<=10:
              x+=matriz[l][c]
if oper=="M":
    for l in range(12):
        for c in range(12):
            if l>c and l+c<=10:
              x+=matriz[l][c]
    x=float(x/30)
print("{:.1f}".format(x))
