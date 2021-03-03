# https://www.urionlinejudge.com.br/judge/pt/problems/view/1080

x=int(input()) 
maior=int(0)
maior=x
p=1
for s in range(2,101):
    x=int(input())
    if x>maior:
        maior=x
        p=s
print(maior)
print(p)
