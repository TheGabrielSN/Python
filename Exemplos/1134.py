# https://www.urionlinejudge.com.br/judge/pt/problems/view/1134

al = ga = di = 0
while True:
          a = int(input())
          if a == 1:
                    al += 1
          elif a == 2:
                    ga += 1
          elif a == 3:
                    di += 1
          elif a == 4:
                    break
print("MUITO OBRIGADO\nAlcool: {}\nGasolina: {}\nDiesel: {}".format(al, ga, di))
