import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import CENTER

from utils.play_sound import play_audio_thread


class MathGameFrame:
    back_frame_for_button_back: tk.Frame

    def __init__(self, parent, bg):
        self.timer = 0

        self.math_game_frame = tk.Frame(parent, bg=bg)
        self.math_game_frame_title = ttk.Label(self.math_game_frame, text='Solve the example:', background='black',
                                               foreground='#4eff00', font=('Lucida Console', 20))

        self.example_label = ttk.Label(self.math_game_frame, text='67 + 198 = ?', background='black',
                                       foreground='#4eff00', font=('Lucida Console', 20))
        self.example_label.example_text = ''  # создание своего атрибута в виджете для хранения имени видджета

        self.answer_entry_label = ttk.Label(self.math_game_frame, text='Your answer:', background='black',
                                            foreground='#4eff00', font=('Lucida Console', 20))
        self.answer_entry = tk.Entry(self.math_game_frame, background='black',
                                     foreground='#4eff00', bd=5, insertbackground='#4eff00',
                                     font=('Lucida Console', 14))
        self.answer_entry_help = ttk.Label(self.math_game_frame, text='', background='black',
                                           foreground='red', font=('Lucida Console', 12))

        self.answer_button = tk.Button(self.math_game_frame, text='Answer', font=('Lucida Console', 14),
                                       command=self._answer)

        self.points_label = ttk.Label(self.math_game_frame, text='Your points: ', background='black',
                                      foreground='#4eff00', font=('Lucida Console', 20))
        self.timer_label = ttk.Label(self.math_game_frame, text='Timer: 60 seconds', background='black',
                                     foreground='#4eff00', font=('Lucida Console', 20))

        self.play_again_button = tk.Button(self.math_game_frame, text='Play Again!', font=('Lucida Console', 14),
                                           command=self._play_again)

        self.back_frame_for_button_back = ''
        self.button_back = tk.Button(self.math_game_frame, text='Return to Game Mode',
                                     font=('Lucida Console', 14),
                                     command=self._load_back_frame)

        self._render_frame()

    def _render_frame(self):
        self.math_game_frame.place(anchor='center', relx=0.5, rely=0.5, relwidth=1, relheight=1)
        self.math_game_frame_title.place(anchor=CENTER, relx=0.5, rely=0.1)
        self.example_label.place(anchor=CENTER, relx=0.5, rely=0.25)
        self.answer_entry_label.place(anchor=CENTER, relx=0.5, rely=0.35)
        self.answer_entry.place(anchor=CENTER, relx=0.5, rely=0.45)
        self.answer_entry_help.place(anchor=CENTER, relx=0.5, rely=0.5)
        self.answer_button.place(anchor=CENTER, relx=0.5, rely=0.6)
        self.points_label.place(anchor=CENTER, relx=0.5, rely=0.7)
        self.timer_label.place(anchor=CENTER, relx=0.5, rely=0.8)
        self.play_again_button.place(anchor=CENTER, relx=0.5, rely=0.9)
        self.play_again_button.place(anchor=CENTER, relx=0.5, rely=0.95)

    def _load_back_frame(self):
        play_audio_thread('sounds/button_click.wav')
        if self.back_frame_for_button_back:
            self.back_frame_for_button_back.tkraise()

    def _answer(self):
        pass

    def _play_again(self):
        pass
