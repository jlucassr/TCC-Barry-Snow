A = input()
A = int(A)

for cont in range(0,A):
    num = int(input())
    i = 0
    j = 1
    while j <= num:
        if num % j == 0:
            i = i + 1
        j = j + 1
    if i > 2:
        print("{} nao eh primo".format(num))
    else:
        print("{} eh primo".format(num))