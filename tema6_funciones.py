import os

def funcion1():
    os.system('cls')
    print("Dame 2 numeros: ")
    num1= int(input("Primer numero: "))
    num2 = int(input("Segundo numero: "))
    print("La suma de los dos numeros es: ", num1 + num2)


def funcion2():
    os.system('cls')
    print("Dame 2 numeros: ")
    num1= int(input("Primer numero: "))
    num2 = int(input("Segundo numero: "))
    print("La resta de los dos numeros es: ", num1 - num2)

def funcion3():
    os.system('cls')
    print("Dame 2 numeros: ")
    num1= int(input("Primer numero: "))
    num2 = int(input("Segundo numero: "))
    print("La multiplicacion de los dos numeros es: ", num1 * num2)  

def funcion4():
    os.system('cls')
    print("Dame 2 numeros: ")
    num1= int(input("Primer numero: "))
    num2 = int(input("Segundo numero: "))
    print("La division de los dos numeros es: ", num1 / num2)      


def run():
    opcion = 0
    while opcion != 5:
        os.system('cls')
        print("Menu de operaciones: ")
        print("1.- Suma")
        print("2.- Resta")
        print("3.- Multiplicacion")
        print("4.- Division")
        print("5.- Salir")
        opcion = int(input("Dame una opcion: "))
    
        if opcion == 1:
            funcion1()
        if opcion == 2:
            funcion2()
        if opcion == 3:
            funcion3()
        if opcion == 4:
            funcion4() 
        if opcion == 5:
            print("Saliendo del programa.")
        if opcion != 5:
            input("\nPresiona Enter para continuar...")       
    

if __name__ == "__main__":
    run()