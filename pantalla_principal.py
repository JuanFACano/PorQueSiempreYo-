import customtkinter as ct

PIECES = 30


class PantallaPrincipal(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title("Inicio")
        self.geometry("1280x720")
        self.resizable(0, 0)
        self.configure(fg_color="#4557B5")
        self.grid_columnconfigure((0), weight=1)
        self.grid_columnconfigure((1), weight=2)
        self.grid_rowconfigure(0, weight=1)

        # Variables
        self.var = 1
        self.entries = []
        self.labels = []
        self.message = []
        self.values = []
        self.pieces = []

        # Titulo
        self.title_init = ct.CTkLabel(
            self, text="POR QUE\nSIEMPRE\nYO?", font=("copyduck", 120)
        )
        self.title_init.grid(row=0, column=0, padx=20, pady=(40, 40), sticky="nsew")

        # sección jugadores
        self.tab_players = ct.CTkFrame(self, fg_color="#E2E9F7")
        self.tab_players.grid(row=0, column=1, padx=40, pady=(40, 40), sticky="nsew")
        self.tab_players.grid_rowconfigure((0), weight=1)
        self.tab_players.grid_rowconfigure((1), weight=1)
        self.tab_players.grid_rowconfigure((2), weight=1)
        self.tab_players.grid_columnconfigure(0, weight=1)

        # header - numero de jugadore
        self.tab_players_title = ct.CTkFrame(self.tab_players, fg_color="transparent")
        self.tab_players_title.grid(row=0, column=0, sticky="nsew")
        self.tab_players_title.grid_columnconfigure((0), weight=1)
        self.tab_players_title.grid_columnconfigure((2), weight=1)
        self.tab_players_title.grid_rowconfigure((0), weight=5)
        self.tab_players_title.grid_rowconfigure((1), weight=1)
        self.tab_players_title.grid_rowconfigure((2), weight=1)

        self.tab_players_entries = ct.CTkFrame(self.tab_players, fg_color="transparent")
        self.tab_players_entries.grid(row=1, column=0, sticky="nsew")
        self.tab_players_entries.grid_columnconfigure((0), weight=1)

        # titulo - numero de jugadore
        self.players = ct.CTkLabel(
            self.tab_players_title,
            text="Ingresa el numero\nde jugadores\nmin 2 - max 6",
            font=("copyduck", 24),
            text_color="#000000",
        )
        self.players.grid(row=0, column=1, sticky="nsew")

        # Ingresar - numero de jugadore
        self.tab_entry = ct.CTkFrame(self.tab_players_title, fg_color="transparent")
        self.tab_entry.grid(row=1, column=1, sticky="nsew")
        self.tab_entry.grid_columnconfigure((0), weight=3)
        self.tab_entry.grid_columnconfigure((1), weight=1)
        self.tab_entry.grid_rowconfigure((0), weight=1)

        self.num_players = ct.CTkEntry(
            self.tab_entry,
            width=50,
            corner_radius=20,
            border_color="#000000",
            border_width=1,
            fg_color="#ffffff",
            text_color="#000000",
            font=("copyduck", 24),
            justify="center",
        )
        self.num_players.grid(row=0, column=0, sticky="nsew", padx=10)

        self.button_num_players = ct.CTkButton(
            self.tab_entry,
            text="Seleccionar",
            width=10,
            fg_color="#4557B5",
            font=("copyduck", 16),
            command=self.create_entry_players,
        )
        self.button_num_players.grid(row=0, column=1, sticky="nsew")

        # Boton para empezar juego
        self.button_play_game = ct.CTkButton(
            self.tab_players,
            text="Comenzar Juego",
            fg_color="#4557B5",
            font=("copyduck", 16),
            command=self.play_game,
        )
        self.button_play_game.grid(row=2, column=0, ipadx=10, ipady=10)

    # Crear los campos para ingresar nombre
    def create_entry_players(self):

        self.toggle_label_entry()
        num_players = self.validate_players()
        if num_players is not None:
            for i in range(num_players):
                frame = ct.CTkFrame(
                    self.tab_players_entries, height=40, fg_color="transparent"
                )
                frame.grid(row=i, column=0, padx=10, pady=5)
                label = ct.CTkLabel(
                    frame,
                    text=f"jugador {i+1}",
                    font=("copyduck", 18),
                    text_color="#000000",
                )
                entry = ct.CTkEntry(
                    frame,
                    width=200,
                    height=30,
                    placeholder_text="Nombre Jugador",
                    corner_radius=20,
                    fg_color="#ffffff",
                    border_width=1,
                    justify="center",
                    text_color="#000000",
                    font=("copyduck", 16),
                )
                self.entries.append(entry)
                self.labels.append(label)

            self.show_label_entry_players()

    # Mostrar los campos para ingresar nombre
    def show_label_entry_players(self):
        for label in self.labels:
            label.grid(row=0, column=0)
        for entry in self.entries:
            entry.grid(row=0, column=1, padx=10, ipadx=10)

    # verificar que lo ingresado sea valido
    def validate_players(self):
        entry = self.num_players.get()

        if not entry.isdigit():
            if len(entry) == 0:
                label = ct.CTkLabel(
                    self.tab_players_title,
                    text="xDios, escribe algo,\n¿Estas bien?",
                    font=("copyduck", 18),
                    text_color="#000000",
                )
            else:
                label = ct.CTkLabel(
                    self.tab_players_title,
                    text=f"xDios, ' {entry} ' no es un numero,\n¿Estas bien?",
                    font=("copyduck", 18),
                    text_color="#000000",
                )
        else:
            entry = int(self.num_players.get())
            if entry < 2 or entry > 6:
                label = ct.CTkLabel(
                    self.tab_players_title,
                    text=f"xDios, ' {entry} ' no esta entre 2 y 6,\n¿Que te pasa?",
                    font=("copyduck", 18),
                    text_color="#000000",
                )
            else:
                for message in self.message:
                    message.destroy()
                return entry
        label.grid(row=2, column=1, sticky="nsew", pady=20)
        self.message.append(label)
        return None

    # verificar widget visible
    def toggle_label_entry(self):
        for entry in self.entries:
            if entry.grid_info():  # Verifica si el widget está actualmente visible
                entry.destroy()

        for label in self.labels:
            if label.grid_info():  # Verifica si el widget está actualmente visible
                label.destroy()
        self.entries = []
        self.labels = []

    def splitting_pieces(self, num_players):
        pieces = int(PIECES / num_players)

        for _ in range(num_players):
            self.pieces.append(pieces)

    # Mostrar valores de los entries
    def play_game(self):
        values = self.get_value_entries(self.entries)
        self.splitting_pieces(len(values))

        for i, value in enumerate(values):
            self.values.append([value, self.pieces[i]])
        self.destroy()

    # Tomar el valor de las entradas
    def get_value_entries(self, entries):
        valores = []
        for entry in entries:
            value = entry.get()
            valores.append(value)
        return valores
