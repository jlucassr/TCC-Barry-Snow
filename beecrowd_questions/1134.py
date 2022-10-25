dicto = {"Alcool": 0, "Gasolina": 0, "Diesel": 0}

i = int(input())
while i != 4:
    if i == 1:
        dicto["Alcool"] += 1
    elif i == 2:
        dicto["Gasolina"] += 1
    elif i == 3:
        dicto["Diesel"] += 1
    i = int(input())

print("MUITO OBRIGADO")
print("Alcool:", dicto["Alcool"])
print("Gasolina:", dicto["Gasolina"])
print("Diesel:", dicto["Diesel"])