from Equipo import Equipo
from Arquero import Arquero
from JugadorCampo import JugadorCampo

def pedir_numero(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isdigit():
            return int(valor)
        else:
            print(" Solo se permiten números. Intente nuevamente.")

def pedir_opcion_posicion():
    while True:
        print("Posición: 1-Arquero 2-Defensor 3-Central 4-Delantero")
        pos = input("Seleccione posición: ")
        if pos in ["1", "2", "3", "4"]:
            return pos
        else:
            print(" Ingrese una opción válida (1-2-3-4).")

def menu_estadisticas(equipo):
    while True:
        print("\n--- ESTADÍSTICAS ADICIONALES ---")
        print("1. Tabla de goleadores")
        print("2. Mayor goleador")
        print("3. Cantidad de jugadores por posición")
        print("4. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            equipo.tabla_goleadores()
        elif opcion == "2":
            equipo.mayor_goleador()
        elif opcion == "3":
            equipo.cantidad_por_posicion()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

def menu():
    equipo = Equipo()
    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar jugador")
        print("2. Mostrar jugadores")
        print("3. Buscar jugador por apellido")
        print("4. Editar jugador")
        print("5. Borrar jugador")
        print("6. Estadísticas adicionales")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numero = pedir_numero("Número de camiseta: ")
            apellido = input("Apellido: ")
            minutos = pedir_numero("Minutos jugados: ")
            pos = pedir_opcion_posicion()

            if pos == "1":
                jugador = Arquero(numero, apellido, minutos)
            else:
                goles = pedir_numero("Cantidad de goles: ")
                if pos == "2":
                    posicion = "Defensor"
                elif pos == "3":
                    posicion = "Central"
                elif pos == "4":
                    posicion = "Delantero"
                jugador = JugadorCampo(numero, apellido, posicion, minutos, goles)

            equipo.agregar_jugador(jugador)

        elif opcion == "2":
            equipo.mostrar_jugadores()

        elif opcion == "3":
            apellido = input("Ingrese apellido a buscar: ")
            equipo.buscar_por_apellido(apellido)

        elif opcion == "4":
            numero = pedir_numero("Ingrese número de camiseta a editar: ")
            equipo.editar_jugador(numero)

        elif opcion == "5":
            numero = pedir_numero("Ingrese número de camiseta a borrar: ")
            equipo.borrar_jugador(numero)

        elif opcion == "6":
            menu_estadisticas(equipo)

        elif opcion == "7":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")

# Ejecutar programa
if __name__ == "__main__":
    menu()
