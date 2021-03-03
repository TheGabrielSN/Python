# https://www.urionlinejudge.com.br/judge/pt/problems/view/2582

l = ["PROXYCITY","P.Y.N.G.","DNSUEY!","SERVERS","HOST!","CRIPTONIZE","OFFLINE DAY","SALT","ANSWER!","RAR?","WIFI ANTENNAS",]
x = int(input())
for i in range(x):
    n1,n2 = map(int, input().split())
    if (n1+n2 >= 0) and (n1+n2 <= 10):
        print(l[(n1+n2)])
