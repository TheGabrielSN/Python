# https://www.urionlinejudge.com.br/judge/pt/problems/view/1040

n1,n2,n3,n4=map(float,input().split())
s=((n1*2)+(n2*3)+(n3*4)+(n4*1))/10
print("Media: {:.1f}".format(s))
if s>=7.0:
    print("Aluno aprovado.")
if s<5.0:
    print("Aluno reprovado.")
if s<=6.9 and s>=5.0:
    print("Aluno em exame.")
    e=float(input())
    print("Nota do exame: {:.1f}".format(e))
    s=(s+e)/2
    if s>=5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: {:.1f}".format(s))