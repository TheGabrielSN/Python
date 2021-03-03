# https://www.urionlinejudge.com.br/judge/pt/problems/view/1828

#lista=["pedra","papel","tesoura","lagarto","spock"]
num=int(input())
for i in range(num):
    j1,j2=map(str, input().split())
    if (j1=="tesoura" and j2=="papel") or (j1=="papel" and j2=="pedra") or (j1=="pedra" and j2=="lagarto") or (j1=="lagarto" and j2=="Spock") or (j1=="Spock" and j2=="tesoura") or (j1=="tesoura" and j2=="lagarto") or (j1=="lagarto" and j2=="papel") or (j1=="papel" and j2=="Spock") or (j1=="Spock" and j2=="pedra") or (j1=="pedra" and j2=="tesoura") :
        print("Caso #{}: Bazinga!".format(i+1))
    if (j2=="tesoura" and j1=="papel") or (j2=="papel" and j1=="pedra") or (j2=="pedra" and j1=="lagarto") or (j2=="lagarto" and j1=="Spock") or (j2=="Spock" and j1=="tesoura") or (j2=="tesoura" and j1=="lagarto") or (j2=="lagarto" and j1=="papel") or (j2=="papel" and j1=="Spock") or (j2=="Spock" and j1=="pedra") or (j2=="pedra" and j1=="tesoura") :
        print("Caso #{}: Raj trapaceou!".format(i+1))
    if j1==j2:
        print("Caso #{}: De novo!".format(i+1))
