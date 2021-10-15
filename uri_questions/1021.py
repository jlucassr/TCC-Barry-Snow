def notas100(total_int):
    return total_int//10000

def notas50(total_int):
    return 

total = float(input())
total_int = int(total * 100)

notas100reais = notas100(total_int)
notas50reais = (total_int%10000)//5000
notas20reais = (total_int%10000)%5000//2000
notas10reais = (total_int%10000)%5000%2000//1000
notas5reais = (total_int%10000)%5000%2000%1000//500
notas2reais = (total_int%10000)%5000%2000%1000%500//200

moeda1real = (total_int%10000)%5000%2000%1000%500%200//100 
moedas50centavos = (total_int%10000)%5000%2000%1000%500%200%100//50
moedas25centavos = (total_int%10000)%5000%2000%1000%500%200%100%50//25
moedas10centavos = (total_int%10000)%5000%2000%1000%500%200%100%50%25//10
moedas5centavos = (total_int%10000)%5000%2000%1000%500%200%100%50%25%10//5
moedas1centavo = (total_int%5)

print("NOTAS:")
print(notas100reais, "nota(s) de R$ 100.00")
print(notas50reais, "nota(s) de R$ 50.00")
print(notas20reais, "nota(s) de R$ 20.00")
print(notas10reais, "nota(s) de R$ 10.00")
print(notas5reais, "nota(s) de R$ 5.00")
print(notas2reais, "nota(s) de R$ 2.00")
print("MOEDAS:")
print(moedas1, "moeda(s) de R$ 1.00")
print(moedas50, "moeda(s) de R$ 0.50")
print(moedas25, "moeda(s) de R$ 0.25")
print(moedas10, "moeda(s) de R$ 0.10")
print(moedas5, "moeda(s) de R$ 0.05")
print(moedas1, "moeda(s) de R$ 0.01")
