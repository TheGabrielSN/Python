# https://www.urionlinejudge.com.br/judge/pt/problems/view/1177

s=[]
x=int(input())
for I in range(1000):
    for i in range(x):
        s.append(i)
    print("N[{}] = {}".format(I,s[I]))
