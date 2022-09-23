
def dibujarA(b,car,esp):
    for f in range (0,b):
        for c in range(0,b):
            if True:
                print(car,end="")
            else:
                print(esp,end="")
        print()

def dibujarB(b,car,esp):
    for f in range (0,b):
        for c in range(0,b):
            if f==b-1 or c==0 or f==0 or c==b-1:
                print(car,end="")
            else:
                print(esp,end="")
        print()

def dibujarC(b,car,esp):
    for f in range (0,b):
        for c in range(0,b):
            if f<=c:
                print(car,end="")
            else:
                print(esp,end="")
        print()

def dibujarD(b,car,esp):
    for f in range (0,b):
        for c in range(0,b):
            if (f+c<=b-1 and f<=c) or (f+c>=b-1 and f>=c):
                print(car,end="")
            else:
                print(esp,end="")
        print()

def dibujarE(b,car,esp):
    for f in range (0,b):
        for c in range(0,b):
            if (f+c>=b-1 and f>=c) or f== b//2 or c== b//2:
                print(car,end="")
            else:
                print(esp,end="")
        print()

def dibujarF(b,car,esp):
    for f in range (0,b):
        for c in range(0,b):
            if f==c or f==0 or f+c==b-1 or f==b-1:
                print(car,end="")
            else:
                print(esp,end="")
        print()

def dibujarG(b,car,esp):
    for f in range (0,b):
        for c in range(0,b):
            if f+(b//2)==c or f-(b//2)==c or f+c-(b//2)==b-1 or f+c+(b//2)==b-1 :
                print(car,end="")
            else:
                print(esp,end="")
        print()
        
def dibujarH(b,car,esp):
    for f in range (0,b):
        for c in range(0,b):
            if f+(b//2)>=c and f-(b//2)<=c and f+c-(b//2)<=b-1 and f+c+(b//2)>=b-1 :
                print(car,end="")
            else:
                print(esp,end="")
        print()

def dibujarI(b,car,esp):
    for f in range (0,b):
        for c in range(0,b):
            if f+(b//2)<=c or f-(b//2)>=c or f+c-(b//2)>=b-1 or f+c+(b//2)<=b-1 :
                print(car,end="")
            else:
                print(esp,end="")
        print()
        

def main():
    b = int(input("Ingrese el lado del cuadrado (debe ser >= 5 e impar)"))
    car = " " + input(" Ingrese un caracter imprimible: ")
    esp = " " + input(" Ingrese un caracter imprimible distinto del anterior: ")
    dibujar(b,car,esp)
    
main()