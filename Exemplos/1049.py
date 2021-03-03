# https://www.urionlinejudge.com.br/judge/pt/problems/view/1049

p1=str(input())
p2=str(input())
p3=str(input())
if p1=='vertebrado' and p2=='ave' and p3=='carnivoro':
    print("aguia")
if p1=='vertebrado' and p2=='ave' and p3=='onivoro':
    print("pomba")
if p1=='vertebrado' and p2=='mamifero' and p3=='herbivoro':
    print("vaca")
if p1=='vertebrado' and p2=='mamifero' and p3=='onivoro':
    print("homem")
if p1=='invertebrado' and p2=='inseto' and p3=='hematofago':
    print("pulga")
if p1=='invertebrado' and p2=='inseto' and p3=='herbivoro':
    print("lagarta")
if p1=='invertebrado' and p2=='anelideo' and p3=='hematofago':
    print("sanguessuga")
if p1=='invertebrado' and p2=='anelideo' and p3=='onivoro':
    print("minhoca")