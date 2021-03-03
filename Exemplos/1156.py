# https://www.urionlinejudge.com.br/judge/pt/problems/view/1156

s=float(1)
x=3
c=2
while True:
    if x>=39:
        break
    else:
        di=(x/c)
        s+=di
        c*=2
        x+=2
print("{:.2f}".format(s))
