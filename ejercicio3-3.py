def comprobarFebrero(d, m, a):
    esBisiesto = (a%4 ==0 and a%100 != 0) or a%400 ==0
    fechaCorrecta = False
    if (esBisiesto and d <= 29) or d <= 28:
        fechaCorrecta = True
    return fechaCorrecta


def comprobarFecha( d, m, a):
    if m==2:
        fechaCorrecta = comprobarFebrero(d, m, a)
    elif ((m%2==1 and m>=7) or (m%2==0 and (m<7 and m <= 12))) and (d > 0 and d <=31):
        fechaCorrecta = True
    elif ((m%2==0 and m>=7) or (m%2==1 and (m<7 and m <= 12))) and (d > 0 and d <=30):
        fechaCorrecta = True
    else:
        fechaCorrecta = False
    return fechaCorrecta