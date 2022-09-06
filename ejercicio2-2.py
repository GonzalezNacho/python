#def chequearNumeroDeTresCifras(a):
    
    
def producto (a, b):
    print("\n{:10}".format(a))
    print("{:5}{:5}".format("x",b))
    print("----------")
    print("{:10}".format(a*(int(str(b)[2]))))
    print("{}{:8}{}".format("+",a*(int(str(b)[1])) ,"-"))
    print("{:8}{}{}".format(a*(int(str(b)[0])) ,"-" ,"-"))
    print("----------")
    print("{:10}".format(a*b))
    

def main():
    multiplicando = int(input("Ingrese el multiplicando: "))
    multiplicador = int(input("Ingrese el multiplicador: "))
    producto(multiplicando, multiplicador)

main()