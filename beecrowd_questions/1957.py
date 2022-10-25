def hexadecimal(n):
    n = hex(n)
    n = n[2:]
    return n

n = int(input())
a = hexadecimal(n)
print(a.upper())