# https://www.urionlinejudge.com.br/judge/pt/problems/view/1114

while True:
    senha=int(2002)
    x=int(input())
    if x==senha:
        print("Acesso Permitido")
        break 
    if x!=senha:
        print("Senha Invalida")
