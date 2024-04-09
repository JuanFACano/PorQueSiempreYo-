import customtkinter as ct
from PIL import Image


class TabPlayers(ct.CTk):
    def __init__(self, master, players):
        super().__init__()
        self.players = players
        self.tab_players = ct.CTkFrame(
            master=master,
            fg_color="transparent",
        )

        self.tab_players.grid(
            row=0, column=1, padx=(0, 20), pady=(20, 20), sticky="nsew"
        )
        self.tab_players.grid_rowconfigure((0), weight=2)
        self.tab_players.grid_columnconfigure((0), weight=1)

        self.tab_players_detail = ct.CTkFrame(
            master=self.tab_players,
            border_width=2,
            border_color="#242847",
            corner_radius=20,
            fg_color="transparent",
        )
        self.tab_players_detail.grid(row=0, column=0, sticky="nsew")
        self.tab_players_detail.grid_rowconfigure((0), weight=1)
        self.tab_players_detail.grid_rowconfigure((1), weight=2)
        self.tab_players_detail.grid_columnconfigure((0), weight=1)

        self.tab_random = ct.CTkFrame(
            master=self.tab_players,
            border_width=2,
            border_color="#242847",
            corner_radius=20,
            fg_color="transparent",
        )
        self.tab_random.grid(row=1, column=0, sticky="nsew")

        # Title
        self.players_title = ct.CTkLabel(
            master=self.tab_players_detail,
            text="Jugadores",
            font=("copyduck", 48),
            text_color="#242847",
        )

        self.players_title.grid(row=0, column=0, sticky="ew", padx=20)

        self.tab_player = ct.CTkFrame(
            master=self.tab_players_detail, fg_color="transparent"
        )
        self.tab_player.grid(row=1, column=0, sticky="nsew", padx=10)
        self.tab_player.grid_columnconfigure((0), weight=1)
        contador = 1
        for players in self.players:
            for player in players:
                tab_player = ct.CTkFrame(master=self.tab_player, fg_color="transparent")
                label_name = ct.CTkLabel(
                    master=tab_player,
                    text=f"{contador}.   {player[0]}",
                    font=("copyduck", 32),
                    text_color="#242847",
                )
                label_piece = ct.CTkLabel(
                    master=tab_player,
                    text=f"{player[1]}",
                    font=("copyduck", 32),
                    text_color="#242847",
                )
                contador += 1
                tab_player.grid(row=contador - 1, column=0, sticky="ew")
                tab_player.grid_columnconfigure((0), weight=1)
                tab_player.grid_columnconfigure((1), weight=1)

                label_name.grid(row=0, column=0, padx=20, sticky="w")
                label_piece.grid(row=0, column=1, padx=20, sticky="e")

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
