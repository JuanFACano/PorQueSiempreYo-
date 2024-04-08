import customtkinter as ct

from tab_game import TabGame
from tab_player import TabPlayer


class Tablero(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title("¿Por Qué Siempre Yo?")
        self.geometry("1280x720")
        self.resizable(0, 0)
        self.configure(fg_color="#A9C0E7")
        self.grid_columnconfigure((0), weight=5)
        self.grid_columnconfigure((1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.tab_game = TabGame(self)
        self.tab_game = TabPlayer(self)