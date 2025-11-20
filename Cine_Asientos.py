import os

def limpiar_pantalla():
    """Limpia la consola para una mejor visualización."""
    os.system('cls' if os.name == 'nt' else 'clear')

def crear_sala(filas, columnas):
    """Crea una matriz de filas x columnas llena de 'L'."""
    return [["L" for _ in range(columnas)] for _ in range(filas)]

def mostrar_sala(sala):
    """Imprime la matriz con formato bonito, incluyendo números de guía."""
    filas = len(sala)
    columnas = len(sala[0])

    print("\n--- PANTALLA ---")
    # Imprimir números de columna
    print("  ", end=" ")
    for c in range(columnas):
        print(f"{c + 1}", end=" ")
    print()

    # Imprimir filas con su número
    for i in range(filas):
        print(f"{i + 1} |", end=" ") # Número de fila
        for asiento in sala[i]:
            print(asiento, end=" ")
        print("|")
    print("-" * (columnas * 2 + 5))

def reservar_asiento(sala):
    try:
        f = int(input("Ingrese número de fila: ")) - 1
        c = int(input("Ingrese número de columna: ")) - 1

        # Validar que el asiento exista (esté dentro de los límites)
        if 0 <= f < len(sala) and 0 <= c < len(sala[0]):
            if sala[f][c] == "L":
                sala[f][c] = "X"
                print(f"✅ ¡Éxito! Asiento en Fila {f+1}, Columna {c+1} reservado.")
            else:
                print(f"❌ El asiento Fila {f+1}, Columna {c+1} ya está OCUPADO.")
        else:
            print("❌ Error: Esa fila o columna no existe en la sala.")
    except ValueError:
        print("❌ Error: Por favor ingrese números válidos.")

def liberar_asiento(sala):
    try:
        f = int(input("Ingrese número de fila a liberar: ")) - 1
        c = int(input("Ingrese número de columna a liberar: ")) - 1

        # Validar límites
        if 0 <= f < len(sala) and 0 <= c < len(sala[0]):
            if sala[f][c] == "X":
                sala[f][c] = "L"
                print(f"✅ Asiento en Fila {f+1}, Columna {c+1} liberado.")
            else:
                print(f"ℹ️ El asiento ya estaba libre.")
        else:
            print("❌ Error: Esa fila o columna no existe.")
    except ValueError:
        print("❌ Error: Por favor ingrese números válidos.")

def mostrar_estadisticas(sala):
    ocupados = sum(fila.count("X") for fila in sala)
    totales = len(sala) * len(sala[0])
    libres = totales - ocupados

    print("\n📊 ESTADÍSTICAS DE LA SALA")
    print(f"Total de asientos: {totales}")
    print(f"Asientos Ocupados (X): {ocupados}")
    print(f"Asientos Libres   (L): {libres}")

def main():
    print("🎬 BIENVENIDO AL SISTEMA DE CINE 🎬")
    try:
        filas = int(input("Ingrese número de filas del cine: "))
        cols = int(input("Ingrese número de asientos por fila: "))
    except ValueError:
        print("Debe ingresar números enteros. Reinicie el programa.")
        return

    sala = crear_sala(filas, cols)

    while True:
        print("\n" + "="*30)
        print("       MENÚ PRINCIPAL       ")
        print("="*30)
        print("1. Mostrar sala")
        print("2. Reservar asiento")
        print("3. Liberar asiento")
        print("4. Contar asientos ocupados y libres")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            mostrar_sala(sala)
        elif opcion == "2":
            reservar_asiento(sala)
        elif opcion == "3":
            liberar_asiento(sala)
        elif opcion == "4":
            mostrar_estadisticas(sala)
        elif opcion == "5":
            print("¡Gracias por usar el sistema! Hasta luego. 👋")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()