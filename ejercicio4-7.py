def figuraA(b,car,esp):
    for f in range (0,b):
        for c in range(0,b):
            if True:
                print(car,end="")
            else:
                print(esp,end="")
        print()

def figuraB(b,car,esp):
    for f in range (0,b):
        for c in range(0,b):
            if f==b-1 or c==0 or f==0 or c==b-1:
                print(car,end="")
            else:
                print(esp,end="")
        print()

def figuraC(b,car,esp):
    for f in range (0,b):
        for c in range(0,b):
            if f<=c:
                print(car,end="")
            else:
                print(esp,end="")
        print()

def figuraD(b,car,esp):
    for f in range (0,b):
        for c in range(0,b):
            if f>=b//2 :
                print(car,end="")
            else:
                print(esp,end="")
        print()

        
#figuraB(5," *","  ")