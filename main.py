import math

import customtkinter as ct
from PIL import Image


class Main(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title("¿Por Qué Siempre Yo?")
        self.geometry("1280x720")
        self.resizable(0, 0)
        self.configure(fg_color="#A9C0E7")
        self.grid_columnconfigure((0), weight=5)
        self.grid_columnconfigure((1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.tab_game = ct.CTkFrame(
            master=self,
            fg_color="transparent",
        )
        self.tab_game.grid(row=0, column=0, padx=20, pady=(20, 20), sticky="nsew")

        self.tab_players = ct.CTkFrame(
            master=self,
            fg_color="transparent",
        )

        self.tab_players.grid(
            row=0, column=1, padx=(0, 20), pady=(20, 20), sticky="nsew"
        )

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

        # Divisiones Tab_Players
        self.tab_players_detail = ct.CTkFrame(
            master=self.tab_players,
            border_width=2,
            border_color="#242847",
            corner_radius=20,
            fg_color="transparent",
        )

        self.tab_random = ct.CTkFrame(
            master=self.tab_players,
            height=275,
            border_width=2,
            border_color="#242847",
            corner_radius=20,
            fg_color="transparent",
        )

        self.tab_players_detail.pack(expand=True, fill="both", pady=(10, 10))
        self.tab_random.pack(fill="both", pady=(10, 10), ipady=20)

        # Title
        self.players_title = ct.CTkLabel(
            master=self.tab_players_detail,
            text="Jugadores",
            font=("arial", 32, "bold"),
            text_color="#242847",
        )
        self.players_title.pack(pady=(20, 0))

        self.tab_player = ct.CTkFrame(
            master=self.tab_players_detail, fg_color="transparent"
        )
        self.tab_player.pack(expand=True)

        self.players = [
            ["Juan", 5],
            ["carlos", 5],
            ["Tomas", 5],
            ["Jhon", 5],
            ["Andres", 5],
            ["Mario", 5],
        ]

        contador = 1
        for player in self.players:
            label = ct.CTkLabel(
                master=self.tab_player,
                text=f"{contador}. {player[0]}      {player[1]}",
                font=("satoshi", 24, "bold"),
                text_color="#242847",
            )
            contador += 1
            label.pack()

        # Image Dice
        self.image = ct.CTkImage(
            light_image=Image.open("img/gameDice1.png"),
            dark_image=Image.open("img/gameDice1.png"),
            size=(120, 120),
        )
        self.label_image = ct.CTkLabel(
            master=self.tab_random, text="", image=self.image
        )
        self.label_image.pack(pady=20)

        # Button Game
        self.button_turn = ct.CTkButton(
            master=self.tab_random,
            text="Girar Dado",
            fg_color="#3C4791",
            width=250,
            height=50,
        )
        self.button_turn.pack()


app = Main()
app.mainloop()
