# https://www.urionlinejudge.com.br/judge/pt/problems/view/1848

def converterb_d(n):
    decimal = 0
    n = str(n)
    n = n[::-1]
    tam = len(n)
    for i in range(tam):
        if n[i] == "1":
            decimal = decimal + 2**i
    return decimal
saida=0
while True:
    try:
        txt=input()
        if txt=="caw caw":
            print(saida)
            saida=0
        else:
            aux=""
            for i in txt:
                if i=="-":
                    aux+="0"
                if i=="*":
                    aux+="1"
            saida+= int(converterb_d(aux))
    except:
            break
