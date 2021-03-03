# https://www.urionlinejudge.com.br/judge/pt/problems/view/1144

x=int(input())
n1=1
for i in range(1,(x*2)+1):
    if i%2==0:
        print("{} {} {}".format(n1,(n1**2)+1,(n1**3)+1))
        n1+=1
    else:
        print("{} {} {}".format(n1,n1**2,n1**3))
