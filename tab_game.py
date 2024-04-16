import math

import customtkinter as ct

from espacio import Espacio


class TabGame(ct.CTk):
    def __init__(self, master):
        super().__init__()
        self.tab_game = ct.CTkFrame(master=master, fg_color="transparent")
        self.tab_game.grid(row=0, column=0, padx=20, pady=(20, 20), sticky="nsew")
        self.tab_game.grid_columnconfigure((0), weight=1)
        self.tab_game.grid_rowconfigure((0), weight=1)

        self.groups = []

    def crear_tablero(self):
        print("Creando Tablero")
        # Creacion de Canva para Tab_game
        canva = ct.CTkCanvas(
            master=self.tab_game, highlightbackground="#242847", bg="#A9C0E7", width=100
        )
        # self.create_group(1, 1, canva)

        canva.grid(row=0, column=0, sticky="nsew")

    def create_group(self, group_id, num_spaces, canva, posx_inicial, posy_inicial):
        for i in range(num_spaces):
            espacios = canva.create_aa_circle(
                (posx_inicial * (i + 1)), 175, 50, math.pi / 2, fill="#ffffff"
            )
        self.groups.append([espacios, group_id])
