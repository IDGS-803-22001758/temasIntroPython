import os

class Diccionario:
    archivo=""
    palabraEs=""
    palabraIng=""


    def __init__(self):
        self.archivo = "diccionario.txt"
        self.palabraEs=[]
        self.palabraIng=[]

    def capturar(self):
        os.system('cls')
        print(" Capturar Palabras ")
        palabraEs = input("Ingresa la palabra en español: ").strip()
        palabraIng = input("Ingresa la palabra en inglés: ").strip()

        with open(self.archivo, "a") as archivo:
            archivo.write(f"{palabraEs}:{palabraIng}\n")

        print("Palabra guardada exitosamente. :)")

    def buscar(self):
        os.system('cls')
        print(" Buscador de palabras ")
        print("1.- Buscar en español")
        print("2.- Buscar en inglés")
        opcion = int(input("Elige alguna de las opciones: "))

        palabra = input("Ingresa la palabra que quieres buscar: ")

        encontrado = False
        with open(self.archivo, "r") as archivo:
            for linea in archivo:
                palabraEs, palabraIng = linea.strip().split(":")
                if opcion == 1 and palabra == palabraEs:
                    print(f"Palabra encontrada: {palabraIng}")
                    encontrado = True
                    break
                if opcion == 2 and palabra == palabraIng:
                    print(f"Palabra encontrada: {palabraEs}")
                    encontrado = True
                    break

        if not encontrado:
            print("Palabra no encontrada.")

    def menuPrincipal(self):
        opcion=0
        while opcion != 3:
            os.system('cls')
            print(" Menú Principal ")
            print("1.- Capturar palabras")
            print("2.- Buscar palabras")
            print("3.- Salir")
            opcion = int(input("Elige una opción: "))

            if opcion == 1:
                self.capturar()
            if opcion == 2:
                self.buscar()
            if opcion == 3:
                print("Saliendo del programa...")
                break

            input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    diccionario = Diccionario()
    diccionario.menuPrincipal()
