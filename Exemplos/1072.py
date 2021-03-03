# https://www.urionlinejudge.com.br/judge/pt/problems/view/1072

x=int(input())
e=0
s=0
for i in range(x):
    v=int(input())
    if v>=10 and v<=20:
        e+=1
    else:
        s+=1
print("{} in".format(e))
print("{} out".format(s))
