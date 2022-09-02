def convertir(seg):
    segundos = seg%60
    minutos = 0
    horas = 0
    dias = 0
    cont = 0
    while seg > 60:
        seg = seg//60
        cont = cont + 1
        if cont == 1:
            minutos = seg
        elif cont == 2:
            horas = seg
        else:
            dias = seg
    return str(dias) +" dia(s), " + str(horas) + " hora(s), " + str(minutos) + " minuto(s), " + str(segundos) + " segundos(s)."
        
segundos = int(input("Ingrese tiempo en segundos: "))
print(convertir(segundos))