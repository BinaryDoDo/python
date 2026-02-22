import os
import subprocess

def cabecera():
    # En Linux, 'clear' limpia la terminal
    os.system('clear')
    print("----------------------------------------------------------------------------------")
    print("---                            PARU TOOLS (CachyOS)                            ---")
    print("---                            Python edition 0.1                              ---")
    print("----------------------------------------------------------------------------------")

def pausa():
    input("\nPresiona Enter para volver al menú...")

def menu():
    opcion = "-1"
    while opcion != "0":
        cabecera()
        print("1. Actualizar sistema (Repositorios + AUR)")
        print("2. Buscar e instalar un paquete")
        print("3. Limpiar paquetes antiguos (Ahorrar espacio)")
        print("0. Salir")
        print("----------------------------------------------------------------------------------")
        
        opcion = input("Selecciona una opción [0-3]: ")

        if opcion == "1":
            print("Iniciando actualización completa...")
            # Ejecutamos paru -Syu
            subprocess.run(["paru", "-Syu"])
            pausa()
        
        elif opcion == "2":
            paquete = input("Introduce el nombre del paquete a instalar: ")
            if paquete:
                subprocess.run(["paru", "-S", paquete])
            pausa()
            
        elif opcion == "3":
            print("Limpiando caché de paquetes no instalados...")
            subprocess.run(["paru", "-Sc"])
            pausa()
            
        elif opcion == "0":
            print("Saliendo de Paru Tools. ¡Hasta luego!")
            exit()
            
        else:
            print("Opción no válida. Intenta de nuevo.")
            subprocess.run(["sleep", "1"])

# Arrancar el programa
if __name__ == "__main__":
    menu()