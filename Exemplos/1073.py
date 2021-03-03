# https://www.urionlinejudge.com.br/judge/pt/problems/view/1073

x=int(input())
for i in range(2,x+1,2):
    s=i**2
    print("{}^2 = {}".format(i,s))