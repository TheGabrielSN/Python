# https://www.urionlinejudge.com.br/judge/pt/problems/view/1048

sa=float(input())
if sa>=0 and sa<=400:
    vp=(15*sa)/100
    ns=vp+sa
    rg=ns-sa
    print("Novo salario: {:.2f}".format(ns))
    print("Reajuste ganho: {:.2f}".format(rg))
    print("Em percentual: 15 %")
elif sa>=400.01 and sa<=800:
    vp=(12*sa)/100
    ns=vp+sa
    rg=ns-sa
    print("Novo salario: {:.2f}".format(ns))
    print("Reajuste ganho: {:.2f}".format(rg))
    print("Em percentual: 12 %")
elif sa>=800.01 and sa<=1200:
    vp=(10*sa)/100
    ns=vp+sa
    rg=ns-sa
    print("Novo salario: {:.2f}".format(ns))
    print("Reajuste ganho: {:.2f}".format(rg))
    print("Em percentual: 10 %")
elif sa>=1200.01 and sa<=2000:
    vp=(7*sa)/100
    ns=vp+sa
    rg=ns-sa
    print("Novo salario: {:.2f}".format(ns))
    print("Reajuste ganho: {:.2f}".format(rg))
    print("Em percentual: 7 %")
elif sa>2000:
    vp=(4*sa)/100
    ns=vp+sa
    rg=ns-sa
    print("Novo salario: {:.2f}".format(ns))
    print("Reajuste ganho: {:.2f}".format(rg))
    print("Em percentual: 4 %")
