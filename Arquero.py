from Jugador import Jugador

class Arquero(Jugador):
    def __init__(self, numero, apellido, minutos):
        super().__init__(numero, apellido, "Arquero", minutos)