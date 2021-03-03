# https://www.urionlinejudge.com.br/judge/pt/problems/view/1131

c=0
ci,cg,ce=0,0,0
while True:
    i,g=map(int,input().split())
    c+=1
    if i>g:
        ci+=1
    if g>i:
        cg+=1
    if i==g:
        ce+=1
    print("Novo grenal (1-sim 2-nao)")
    x=int(input())
    if x==2:
        break
print("{} grenais".format(c))
print("Inter:{}".format(ci))
print("Gremio:{}".format(cg))
print("Empates:{}".format(ce))
if ci>cg:
    print("Inter venceu mais")
if cg>ci:
    print("Gremio venceu mais")
if ci==cg:
    print("Nao houve vencedor")
