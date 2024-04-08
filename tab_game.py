import math

import customtkinter as ct


class TabGame(ct.CTk):
    def __init__(self, master):
        super().__init__()
        self.tab_game = ct.CTkFrame(
            master=master,
            fg_color="transparent",
        )
        self.tab_game.grid(row=0, column=0, padx=20, pady=(20, 20), sticky="nsew")

        # Creacion de Canva para Tab_game
        self.canva = ct.CTkCanvas(
            master=self.tab_game,
            highlightbackground="#242847",
            bg="#A9C0E7",
        )
        self.canva.pack(expand=True, fill="both")

        # GroupOne
        self.canva.create_aa_circle(750, 200, 50, math.pi / 2, fill="#ffffff")

        # GroupTwo
        self.canva.create_aa_circle(800, 400, 50, math.pi / 2, fill="#ffffff")
        self.canva.create_aa_circle(910, 400, 50, math.pi / 2, fill="#ffffff")

        # GroupThree
        self.canva.create_aa_circle(750, 600, 50, math.pi / 2, fill="#ffffff")
        self.canva.create_aa_circle(850, 675, 50, math.pi / 2, fill="#ffffff")
        self.canva.create_aa_circle(950, 750, 50, math.pi / 2, fill="#ffffff")

        # GroupFour
        self.canva.create_aa_circle(350, 600, 50, math.pi / 2, fill="#ffffff")
        self.canva.create_aa_circle(200, 600, 50, math.pi / 2, fill="#ffffff")
        self.canva.create_aa_circle(350, 750, 50, math.pi / 2, fill="#ffffff")
        self.canva.create_aa_circle(200, 750, 50, math.pi / 2, fill="#ffffff")

        # groupfive
        self.canva.create_aa_circle(350, 200, 50, math.pi / 2, fill="#ffffff")
        self.canva.create_aa_circle(250, 200, 50, math.pi / 2, fill="#ffffff")

        # GroupSix
        self.canva.create_aa_circle(550, 400, 50, math.pi / 2, fill="#ffffff")
