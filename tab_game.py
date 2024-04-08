import math

import customtkinter as ct


class TabGame(ct.CTk):
    def __init__(self, master):
        super().__init__()
        self.tab_game = ct.CTkFrame(master=master, fg_color="transparent")
        self.tab_game.grid(row=0, column=0, padx=20, pady=(20, 20), sticky="nsew")
        self.tab_game.grid_columnconfigure((0), weight=1)
        self.tab_game.grid_rowconfigure((0), weight=1)

        # Creacion de Canva para Tab_game
        self.canva = ct.CTkCanvas(
            master=self.tab_game, highlightbackground="#242847", bg="#A9C0E7", width=100
        )
        self.canva.grid(row=0, column=0, sticky="nsew")

        # GroupOne
        self.canva.create_aa_circle(700, 175, 50, math.pi / 2, fill="#ffffff")

        # GroupTwo
        self.canva.create_aa_circle(750, 375, 50, math.pi / 2, fill="#ffffff")
        self.canva.create_aa_circle(860, 375, 50, math.pi / 2, fill="#ffffff")

        # GroupThree
        self.canva.create_aa_circle(700, 575, 50, math.pi / 2, fill="#ffffff")
        self.canva.create_aa_circle(800, 650, 50, math.pi / 2, fill="#ffffff")
        self.canva.create_aa_circle(900, 725, 50, math.pi / 2, fill="#ffffff")

        # GroupFour
        self.canva.create_aa_circle(300, 575, 50, math.pi / 2, fill="#ffffff")
        self.canva.create_aa_circle(150, 575, 50, math.pi / 2, fill="#ffffff")
        self.canva.create_aa_circle(300, 725, 50, math.pi / 2, fill="#ffffff")
        self.canva.create_aa_circle(150, 725, 50, math.pi / 2, fill="#ffffff")

        # groupfive
        self.canva.create_aa_circle(300, 120, 50, math.pi / 2, fill="#ffffff")
        self.canva.create_aa_circle(150, 120, 50, math.pi / 2, fill="#ffffff")
        self.canva.create_aa_circle(220, 200, 50, math.pi / 2, fill="#ffffff")
        self.canva.create_aa_circle(300, 275, 50, math.pi / 2, fill="#ffffff")
        self.canva.create_aa_circle(150, 275, 50, math.pi / 2, fill="#ffffff")

        # GroupSix
        self.canva.create_aa_circle(500, 400, 50, math.pi / 2, fill="#ffffff")
