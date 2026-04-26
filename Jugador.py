class Jugador:
    def __init__(self, numero, apellido, posicion, minutos):
        self.numero = numero
        self.apellido = apellido
        self.posicion = posicion
        self.minutos = minutos

    def mostrar_datos(self):
        return f"N°{self.numero} - {self.apellido} ({self.posicion}) - Minutos: {self.minutos}"