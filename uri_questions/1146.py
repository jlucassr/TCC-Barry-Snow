x = int(input())

while x != 0:
    l = []
    for i in range(1,x+1):
        l.append(i)
    print(*l)
    x = int(input())