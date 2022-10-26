meu_pi = 3.14159

x = input().split()
a, b, c = x

a = float(a)
b = float(b)
c = float(c)

tri = a * c / 2
cir = meu_pi * c**2
tra =  (a + b) * c / 2
quad = b**2
ret = a * b

print('TRIANGULO: %.3f' %tri)
print('CIRCULO: %.3f' %cir)
print('TRAPEZIO: %.3f' %tra)
print('QUADRADO: %.3f' %quad)
print('RETANGULO: %.3f' %ret)