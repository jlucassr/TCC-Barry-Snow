x = input().split()
a, b, c = x

b = float(b)
c = float(c)

y = input().split()
d, e, f = y

e = float(e)
f = float(f)

resultado = b * c + e * f

print('VALOR A PAGAR: R$ %.2f' % resultado)