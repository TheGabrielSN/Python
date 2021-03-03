# https://www.urionlinejudge.com.br/judge/pt/problems/view/1178

s=[]
ant=0
x=float(input())
for I in range(100):
    if I==0:
        s.append(x)
        ant=x
    else:
        s.append(ant/2)
        ant=(ant/2)
    print("N[{}] = {:.4f}".format(I,s[I]))
