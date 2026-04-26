from JugadorCampo import JugadorCampo

class Equipo:
    def __init__(self):
        self.jugadores = []

    def agregar_jugador(self, jugador):
        for j in self.jugadores:
            if j.numero == jugador.numero:
                print(f"Ya existe un jugador con el número {jugador.numero}. No se puede duplicar.")
                return
        self.jugadores.append(jugador)
        print("Jugador agregado correctamente.")

    def mostrar_jugadores(self):
        if not self.jugadores:
            print("No hay jugadores cargados.")
        else:
            for j in self.jugadores:
                print(j.mostrar_datos())

    def buscar_por_apellido(self, apellido):
        encontrados = [j for j in self.jugadores if j.apellido.lower() == apellido.lower()]
        if encontrados:
            for j in encontrados:
                print(j.mostrar_datos())
        else:
            print("Jugador no encontrado.")

    def editar_jugador(self, numero):
        for j in self.jugadores:
            if j.numero == numero:
                print("Jugador encontrado:", j.mostrar_datos())
                j.minutos = int(input("Nuevos minutos jugados: "))
                if isinstance(j, JugadorCampo):
                    j.goles = int(input("Nueva cantidad de goles: "))
                print("Jugador editado correctamente.")
                return
        print("Jugador no encontrado.")

    def borrar_jugador(self, numero):
        for j in self.jugadores:
            if j.numero == numero:
                self.jugadores.remove(j)
                print(f"Jugador con número {numero} eliminado.")
                return
        print("Jugador no encontrado.")

    # --- Estadísticas adicionales ---
    def tabla_goleadores(self):
        print("\nTabla de goleadores")
        for j in self.jugadores:
            if isinstance(j, JugadorCampo):
                print(f"{j.apellido} ({j.posicion}) - Goles: {j.goles}")

    def mayor_goleador(self):
        goleadores = [j for j in self.jugadores if isinstance(j, JugadorCampo)]
        if goleadores:
            max_goleador = max(goleadores, key=lambda x: x.goles)
            print(f"\nMayor goleador: {max_goleador.apellido} ({max_goleador.posicion}) - {max_goleador.goles} goles")
        else:
            print("No hay jugadores de campo cargados.")

    def cantidad_por_posicion(self):
        conteo = {"Arquero": 0, "Defensor": 0, "Central": 0, "Delantero": 0}
        for j in self.jugadores:
            conteo[j.posicion] = conteo.get(j.posicion, 0) + 1
        print("\nCantidad de jugadores por posición:")
        for pos, cant in conteo.items():
            print(f"{pos}: {cant}")
            