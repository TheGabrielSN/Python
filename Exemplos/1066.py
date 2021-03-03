# https://www.urionlinejudge.com.br/judge/pt/problems/view/1066

s1=0
s2=0
s3=0
s4=0
for i in range(5):
    n1=float(input())
    if n1%2==0:
        s1+=1
    if n1%2==1:
        s2+=1
    if n1<0:
        s3+=1
    if n1>0:
        s4+=1
print("{} valor(es) par(es)".format(s1))
print("{} valor(es) impar(es)".format(s2))
print("{} valor(es) positivo(s)".format(s4))
print("{} valor(es) negativo(s)".format(s3))
