# https://www.urionlinejudge.com.br/judge/pt/problems/view/1149

l=list(map(int,input().split()))
x=" "
s=0
soma=0
for i in l:
    if x==" ":
        x=i
    else:
        if i>0:
            s=i
            break
for I in range(s):
    soma+=x
    x+=1
print(soma)
