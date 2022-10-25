a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

l = [a,b,c,d,e]

par = 0
imp = 0
pos = 0
neg = 0

for i in l:
    if i % 2 == 0:
        par += 1
    if i % 2 != 0:
        imp += 1
    if i > 0:
        pos += 1
    if i < 0:
        neg += 1

print(par, "valor(es) par(es)")
print(imp, "valor(es) impar(es)")
print(pos, "valor(es) positivo(s)")
print(neg, "valor(es) negativo(s)")