# https://www.urionlinejudge.com.br/judge/pt/problems/view/1180

x=int(input()) 
menor=int(0)
menor=x
p=0
s=[]
s=input().split()
for i in range(1,x):
    if int(s[i])<menor:
        menor=int(s[i])
        p=i
print("Menor valor: {}".format(menor))
print("Posicao: {}".format(p))
