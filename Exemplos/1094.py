# https://www.urionlinejudge.com.br/judge/pt/problems/view/1094

x=int(input())
c=int(0)
r=int(0)
s=int(0)
total=int(0)
for i in range(x):
    n,l=map(str,input().split())
    n=int(n)
    if l=='C':
        c+=n
    if l=='R':
        r+=n
    if l=='S':
        s+=n
total=c+r+s
pc=float((c*100)/total)
pr=float((r*100)/total)
ps=float((s*100)/total)
print("Total: {} cobaias".format(total))
print("Total de coelhos: {}".format(c))
print("Total de ratos: {}".format(r))
print("Total de sapos: {}".format(s))
print("Percentual de coelhos: {:.2f} %".format(pc))
print("Percentual de ratos: {:.2f} %".format(pr))
print("Percentual de sapos: {:.2f} %".format(ps))
