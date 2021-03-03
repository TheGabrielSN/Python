# https://www.urionlinejudge.com.br/judge/pt/problems/view/1155

s=0
c=1
while True:
    if c==101:
        break
    s+=float((1/c))
    c+=1
print("{:.2f}".format(s))
