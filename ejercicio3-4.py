def comprobarDistacia(a, b, c):
    if (a > b):
        if (a > c):
            if (b < c):
                mismaDistancia = (a-c == c-b)
            else:
                mismaDistancia = (a-b == b-c)
        elif (a == c):
            mismaDistancia = False
        else:
            mismaDistancia = (c-a == a-b)
    elif (a == b):
        mismaDistancia = (a == c)
    else:
        if (b > c):
            if (a < c):
                mismaDistancia = (b-c == c-a)
            else:
                mismaDistancia = (b-a == a-c)
        elif (a == c):
            mismaDistancia = False
        else:
            mismaDistancia = (c-b == b-a)
    return mismaDistancia

def main():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    c = int(input("Ingrese el tercer número: "))
    if comprobarDistacia(a, b, c):
        print("\nEstán igualmente distanciados!")
    else:
        print("\nNO Están igualmente distaciados!")

main()