a = int(input())

x = 0
y = 1

l = [x,y]

i = 2

while i < a:
    l.append(x+y)
    temp = y
    y = x+y
    x = temp
    i+=1

print(*l)