def cargarListaManual(lista):
    num = int(input())
    while num != 0:
        if num < 0:
            print("Error, número NO positivo.")
        elif estaEnLista(num, lista):
            print("Error, número repetido.")
        else:
            lista.append(num)
        num = int(input())

def cargarConjuntos(lstA, lstB):
    tipoDeCarga = input(int("1. CARGA MANUAL\n2. CARGA AUTOMATICA"))
    if tipoDeCarga == 1:
        cargarListaManual(lstA)
        cargarListaManual(lstB)
    elif tipoDeCarga == 2:
        
def menu():
    print("1. CARGAR CONJUNTOS\n2. UNION\n3. INTERSECCION\n4. DIFERENCIA (A-B)\n5. DIFERENCIA SIMÉTRICA\n6. SALIR")
    opcion = input(int("Ingrese el valor de la opción:"))
    lstA = []
    lstB = []
    while opcion != 6:
        if opcion == 1:
            cargarConjuntos(lstA, lstB)
        elif opcion == 2:
            union(lstA, lstB)
        elif opcion == 3:
            interseccion(lstA, lstB)
        elif opcion == 4:
            diferenciaA-B(lstA, lstB)
        elif opcion == 5:
            diferenciaSimetrica(lstA, lstB)
        else:
            print("Debes elegir una opcion del 1 al 6")

def main:
    menu()

main()