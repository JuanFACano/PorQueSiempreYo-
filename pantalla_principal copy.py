import customtkinter as ct


class PantallaInicial(ct.CTk):
    def __init__(self):
        super().__init__()

        self.label_num_jugadores = ct.CTkLabel(
            self, text="Selecciona el número de jugadores (2-6):"
        )
        self.label_num_jugadores.pack()

        self.entry_num_jugadores = ct.CTkEntry(self)
        self.entry_num_jugadores.pack()

        self.boton_agregar_nombres = ct.CTkButton(
            self, text="Agregar nombres y empezar", command=self.agregar_nombres
        )
        self.boton_agregar_nombres.pack()

        self.entry_nombres = []
        for i in range(6):  # Máximo de 6 jugadores
            entry = ct.CTkEntry(self)
            entry.pack()
            self.entry_nombres.append(entry)

        self.lista_jugadores = None  # Atributo para almacenar la lista de nombres

    def agregar_nombres(self):
        num_jugadores = int(self.entry_num_jugadores.get())
        self.lista_jugadores = [
            entry.get() for entry in self.entry_nombres[:num_jugadores]
        ]
        self.destroy()  # Cerrar la ventana de configuración
