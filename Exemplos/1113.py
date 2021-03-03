# https://www.urionlinejudge.com.br/judge/pt/problems/view/1113

while True:
    x,y=map(int,input().split())
    if x==y:
        break
    if x>y:
        print("Decrescente")
    if y>x:
        print("Crescente")
