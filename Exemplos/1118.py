# https://www.urionlinejudge.com.br/judge/pt/problems/view/1118

while True:
    while True:
        n1=float(input())
        if n1<0.0 or n1>10.0:
            print("nota invalida")
        elif n1>=0.0 and n1<=10.0:
            break
    while True:
        n2=float(input())
        if n2<0.0 or n2>10.0:
            print("nota invalida")
        elif n2>=0.0 and n2<=10.0:
            break
    media=float((n1+n2)/2)
    print("media = {:.2f}".format(media))
    while True:
        print("novo calculo (1-sim 2-nao)")
        x=int(input())
        if x==1 or x==2:
            break
    if x==2:
        break
