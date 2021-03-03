# https://www.urionlinejudge.com.br/judge/pt/problems/view/1098

i=float(0)
j=1
x=3
d=float(0.0)
while i<=2.1:
    while x>0:
        if i%1==0 or i>1.8:
            print("I={:.0f} J={:.0f}".format(i,j))
        elif i!=2:
            print("I={:.1f} J={:.1f}".format(i,j))
        j+=1
        x-=1
    j=1
    d=d+0.2
    x=3
    i=i+0.2
    j=j+d
