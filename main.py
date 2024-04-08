from pantalla_principal import PantallaPrincipal
from tablero import Tablero


class Main:
    def __init__(self):
        pantalla_inicial = PantallaPrincipal()
        pantalla_inicial.mainloop()

        lista_jugadores = [pantalla_inicial.values]

        self.tablero = Tablero(lista_jugadores)
        self.tablero.mainloop()


app = Main()
