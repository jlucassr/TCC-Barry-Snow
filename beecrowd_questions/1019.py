def conversor(total_seg):
    horas = total_seg / 3600
    minutos = (total_seg % 3600) / 60
    segundos = (total_seg % 3600) % 60
    return [horas, minutos, segundos]

num = int(input())

list_horario = conversor(num)

print("%d:%d:%d" %(list_horario[0] , list_horario[1], list_horario[2]))