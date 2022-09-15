def esPositivoONegativo(num):
    if num < 0:
        msj = "negativo"
    elif num > 0:
        msj = "positivo"
    else:
        msj = "cero"
    return msj

def esEnteroNaturalOReal(num):
    esEntero = "." not in num or num.index(".") + 2 == len(num)
    if esEntero:
        msj = "real"
    else
        msj = "natural"
    return msj

