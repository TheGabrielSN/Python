# https://www.urionlinejudge.com.br/judge/pt/problems/view/1097

I=int(7-2)
F=int(4-2)
for i in range(1,10,2):
    I=I+2
    F=F+2
    for j in range(I,F,-1):
        print("I={} J={}".format(i,j))
