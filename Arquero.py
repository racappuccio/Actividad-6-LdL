from Jugador import Jugador

class JugadorCampo(Jugador):
    def __init__(self, numero, apellido, posicion, minutos, goles):
        super().__init__(numero, apellido, posicion, minutos)
        self.goles = goles

    def mostrar_datos(self):
        return super().mostrar_datos() + f" - Goles: {self.goles}"