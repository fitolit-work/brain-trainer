import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import CENTER


class PlayersFrame:
    def __init__(self, parent, bg, create_frame, load_frame):
        self.players_frame = tk.Frame(parent, bg=bg)
        self.players_label = ttk.Label(self.players_frame, text='Choose Action...', background='black',
                                       foreground='#4eff00', font=('Lucida Console', 20))
        self.players_create_button = tk.Button(self.players_frame, text='Create Player', font=('Lucida Console', 14),
                                               command=lambda frame=create_frame: self._create_player_frame(frame))

        self.players_load_button = tk.Button(self.players_frame, text='Load Player', font=('Lucida Console', 14),
                                             command=lambda frame=load_frame: self._load_player_frame(frame))

        self._render_frame()

    def _render_frame(self):
        self.players_frame.place(anchor='center', relx=0.5, rely=0.5, relwidth=1, relheight=1)
        self.players_label.place(anchor=CENTER, relx=0.5, rely=0.1)
        self.players_create_button.place(anchor=CENTER, relx=0.5, rely=0.5)
        self.players_load_button.place(anchor=CENTER, relx=0.5, rely=0.6)

    @staticmethod
    def _create_player_frame(create_frame):
        create_frame.tkraise()

    @staticmethod
    def _load_player_frame(load_frame):
        load_frame.tkraise()
