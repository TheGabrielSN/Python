# https://www.urionlinejudge.com.br/judge/pt/problems/view/1142

x=int(input())
c=1
for i in range(x):
    print("{} {} {} PUM".format(c,c+1,c+2))
    c+=4
