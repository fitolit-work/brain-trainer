import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import CENTER

from utils.play_sound import play_audio_thread


class MathModeDifficultyFrame:
    back_frame_for_button_back: tk.Frame
    math_game_frame_for_buttons: tk.Frame

    def __init__(self, parent, bg, update_difficulty):
        self.update_difficulty = update_difficulty

        self.math_mode_difficulty_frame = tk.Frame(parent, bg=bg)
        self.math_mode_difficulty_frame_title_label = ttk.Label(self.math_mode_difficulty_frame,
                                                                text='Choose difficulty:', background='black',
                                                                foreground='#4eff00', font=('Lucida Console', 20))

        self.math_mode_difficulty_easy = tk.Button(self.math_mode_difficulty_frame, text='Easy',
                                                   font=('Lucida Console', 14),
                                                   command=lambda difficulty='easy': self._change_difficulty(
                                                       difficulty))
        self.math_mode_difficulty_medium = tk.Button(self.math_mode_difficulty_frame, text='Medium',
                                                     font=('Lucida Console', 14),
                                                     command=lambda difficulty='medium': self._change_difficulty(
                                                         difficulty))
        self.math_mode_difficulty_hard = tk.Button(self.math_mode_difficulty_frame, text='Hard',
                                                   font=('Lucida Console', 14),
                                                   command=lambda difficulty='hard': self._change_difficulty(
                                                       difficulty))
        self.math_mode_difficulty_super_hard = tk.Button(self.math_mode_difficulty_frame, text='Super Hard',
                                                         font=('Lucida Console', 14),
                                                         command=lambda
                                                             difficulty='super hard': self._change_difficulty(
                                                             difficulty))

        self.back_frame_for_button_back = ''
        self.math_game_frame_for_buttons = ''

        self.math_mode_button_back = tk.Button(self.math_mode_difficulty_frame, text='Return to Mode Select',
                                               font=('Lucida Console', 14),
                                               command=self._load_back_frame)

        self._render_frame()

    def _render_frame(self):
        self.math_mode_difficulty_frame.place(anchor='center', relx=0.5, rely=0.5, relwidth=1, relheight=1)
        self.math_mode_difficulty_frame_title_label.place(anchor=CENTER, relx=0.5, rely=0.1)
        self.math_mode_difficulty_easy.place(anchor=CENTER, relx=0.5, rely=0.25)
        self.math_mode_difficulty_medium.place(anchor=CENTER, relx=0.5, rely=0.35)
        self.math_mode_difficulty_hard.place(anchor=CENTER, relx=0.5, rely=0.45)
        self.math_mode_difficulty_super_hard.place(anchor=CENTER, relx=0.5, rely=0.55)

        self.math_mode_button_back.place(anchor=CENTER, relx=0.5, rely=0.85)

    def _change_difficulty(self, difficulty):
        play_audio_thread('sounds/button_click.wav')
        if difficulty == 'easy':
            print('easy')
            self.update_difficulty({'min_number':1, 'max_number':10, 'point':1})
        if difficulty == 'medium':
            print('medium')
            self.update_difficulty({'min_number':5, 'max_number':30, 'point':3})
        if difficulty == 'hard':
            print('hard')
            self.update_difficulty({'min_number':10, 'max_number':70, 'point':6})
        if difficulty == 'super hard':
            print('super hard')
            self.update_difficulty({'min_number':21, 'max_number':199, 'point':10})

        if self.math_game_frame_for_buttons:
            self.math_game_frame_for_buttons.tkraise()

    def _load_back_frame(self):
        play_audio_thread('sounds/button_click.wav')
        if self.back_frame_for_button_back:
            self.back_frame_for_button_back.tkraise()
