# https://www.urionlinejudge.com.br/judge/pt/problems/view/1154

s=float(0)
c=0
while True:
    x=int(input())
    if x<0:
        break
    s+=x
    c+=1
print("{:.2f}".format(s/c))
