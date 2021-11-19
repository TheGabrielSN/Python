#Utilizando for para resolver:
c = 0
k = int(input())
i = int(input())
m = int(input())
n = int(input())
d = int(input())

for num in range(1,d+1):
    if num%k==0:
        c += 1
    elif num%i==0:
        c += 1
    elif num%m==0:
        c += 1
    elif num%n==0:
        c += 1

print(c)


#Utilizando while para resolver:
c = 0
k = int(input())
i = int(input())
m = int(input())
n = int(input())
d = int(input())

num = 1
while num<=d:
    if num%k==0:
        c += 1
    elif num%i==0:
        c += 1
    elif num%m==0:
        c += 1
    elif num%n==0:
        c += 1
print(c)
