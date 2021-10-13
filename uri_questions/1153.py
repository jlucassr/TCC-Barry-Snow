A = input()
A = int(A)

fat = 1

while A >= 1:
    fat = fat * A
    A -= 1

print(fat)