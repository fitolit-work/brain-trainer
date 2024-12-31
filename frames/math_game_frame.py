import threading
import time
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import CENTER

from utils.play_sound import play_audio_thread


class MathGameFrame:
    back_frame_for_button_back: tk.Frame

    def __init__(self, parent, bg):
        self.timer = 60
        self.game = False

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
                                       command=self._get_answer, state='disabled')

        self.points_label = ttk.Label(self.math_game_frame, text='Your points: ', background='black',
                                      foreground='#4eff00', font=('Lucida Console', 20))
        self.timer_label = ttk.Label(self.math_game_frame, text='Timer: ', background='black',
                                     foreground='#4eff00', font=('Lucida Console', 20))

        self.play_again_or_start_button = tk.Button(self.math_game_frame, text='Play!!!', font=('Lucida Console', 14),
                                                    command=self._start_game)

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
        self.button_back.place(anchor=CENTER, relx=0.5, rely=0.87)
        self.play_again_or_start_button.place(anchor=CENTER, relx=0.5, rely=0.96)

    def _load_back_frame(self):
        play_audio_thread('sounds/button_click.wav')
        if self.back_frame_for_button_back:
            self.timer = 0
            self.answer_button['state'] = 'disabled'
            self.play_again_or_start_button['state'] = 'normal'
            self.game = False
            self.timer_label['text'] = f'Timer: '
            self.back_frame_for_button_back.tkraise()

    def _timer_handler(self):
        if self.timer > 0:
            self.timer -= 1
            self.timer_label['text'] = f'Timer: {self.timer} seconds left'
            self.answer_entry_label.after(1000, self._timer_handler)
        else:
            self.answer_button['state'] = 'disabled'
            self.play_again_or_start_button['state'] = 'normal'
            self.timer = 60
            self.game = False
            self.timer_label['text'] = f'Timer: '

    def _start_game(self):
        if not self.game:
            play_audio_thread('sounds/button_click.wav')
            self.game = True
            self.answer_button['state'] = 'normal'
            self.play_again_or_start_button['state'] = 'disabled'
            self.timer_label['text'] = f'Timer: {self.timer} seconds left'
            self.set_new_example()
            self.answer_entry_label.after(1000, self._timer_handler)

    def _get_answer(self):
        play_audio_thread('sounds/button_click.wav')
        print('взять ответ и сравнить с правильным + начислить очки и записатьих в БД')

    def set_new_example(self):
        print('собрать и показать новый пример + вернуть правильный ответ')