# https://www.urionlinejudge.com.br/judge/pt/problems/view/1051

re=float(input())
s=0
if re>=0.00 and re<=2000.00:
    print("Isento")
if re>=2000.01 and re<=3000.00:
    s=(re-2000.00)*0.08
    print("R$ {:.2f}".format(s))
if re>=3000.01 and re<=4500.00:
    s=((re-3000.00)*0.18)+80.00
    print("R$ {:.2f}".format(s))
if re>4500.00:
    s=((re-4500.00)*0.28)+350.00
    print("R$ {:.2f}".format(s))