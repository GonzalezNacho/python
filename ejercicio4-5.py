def esPrimo(num):
    res= True
    if( num == 1 or num%2 ==0):
        res = False
    else:
        for n in range(2, int(num/2)):
            if num % n == 0:
                res = False
    return res
def imprimirHasta (num):
    print(f"primos entre 1 y {num}:")
    for x in range(1,num):
        if (esPrimo(x)):
            print('{:4}'.format(x), end = " ")

def main():
    num= int(input("Ingrese cantidad (numero natural):"))
    imprimirHasta(num)
    

main()