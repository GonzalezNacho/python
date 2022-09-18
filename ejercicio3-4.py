def comprobarDistacia(a, b, c):
    if (a > b):
        if (a > c):
            if (b < c):
                mismaDistancia = (b+a)/2 == c
            else:
                mismaDistancia = (a+c)/2 == b
        elif (a == c):
            mismaDistancia = False
        else:
            mismaDistancia = (c+b)/2 == a
    elif (a == b):
        mismaDistancia = (a == c)
    else:
        if (b > c):
            if (a < c):
                mismaDistancia = (b+a)/2 == c
            else:
                mismaDistancia = (b+c)/2 == a
        elif (a == c):
            mismaDistancia = False
        else:
            mismaDistancia = (c+a)/2 == b
    return mismaDistancia

def main():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    c = int(input("Ingrese el tercer número: "))
    if comprobarDistacia(a, b, c):
        print("\nEstán igualmente distanciados")
    else:
        print("\nNO Están igualmente distaciados")

main()