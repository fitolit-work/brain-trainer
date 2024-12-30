import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import CENTER

from model.db_func import load_user
from utils import checks
from utils.play_sound import play_audio_thread


class GameModeFrame:
    def __init__(self, parent, bg):
        self.game_mode_frame = tk.Frame(parent, bg=bg)
        self.game_mode_title_label = ttk.Label(self.game_mode_frame, text='Select game mode:', background='black',
                                               foreground='#4eff00', font=('Lucida Console', 20))


        self.game_mode_player_label = ttk.Label(self.game_mode_frame, text='Your player:', background='black',
                                               foreground='#4eff00', font=('Lucida Console', 20))

        self.game_mode_player_label.player_name = '' # создание своего атрибута в виджете для хранение имени видджета

        self.math_frame_for_button_mode_math = ''
        self.game_mode_math_button = tk.Button(self.game_mode_frame, text='Math mode', font=('Lucida Console', 14),
                                               command=self._load_math_difficulty_level_frame)
        self.back_frame_for_button_back = ''
        self.game_mode_button_back = tk.Button(self.game_mode_frame, text='Return to Player Select',
                                               font=('Lucida Console', 14),
                                               command=self._load_back_frame)

        self._render_frame()

    def _render_frame(self):
        self.game_mode_frame.place(anchor='center', relx=0.5, rely=0.5, relwidth=1, relheight=1)
        self.game_mode_title_label.place(anchor=CENTER, relx=0.5, rely=0.1)
        self.game_mode_player_label.place(anchor=CENTER, relx=0.5, rely=0.25)
        self.game_mode_math_button.place(anchor=CENTER, relx=0.5, rely=0.6)
        self.game_mode_button_back.place(anchor=CENTER, relx=0.5, rely=0.8)

    def _load_math_difficulty_level_frame(self):
        play_audio_thread('sounds/button_click.wav')
        if self.math_frame_for_button_mode_math:
            self.math_frame_for_button_mode_math.tkraise()

    def _load_back_frame(self):
        play_audio_thread('sounds/button_click.wav')
        if self.back_frame_for_button_back:
            self.back_frame_for_button_back.tkraise()


