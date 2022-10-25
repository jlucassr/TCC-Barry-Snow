dias_ini = int(input())

anos = int(dias_ini/365)

meses = int((dias_ini%365)/30)

dias = int((dias_ini%365)%30)

print(anos, "ano(s)")
print(meses, "mes(es)")
print(dias, "dia(s)")
