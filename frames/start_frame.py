import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import CENTER

from utils.play_sound import play_audio_thread


class StartFrame:
    def __init__(self, parent, bg, next_frame):
        self.start_frame = tk.Frame(parent, bg=bg)
        self.start_label = ttk.Label(self.start_frame, text='Train your mind wisely!', background='black',
                                     foreground='#4eff00', font=('Lucida Console', 20))
        self.start_button = tk.Button(self.start_frame, text='Start game', font=('Lucida Console', 14),
                                      command=lambda frame=next_frame: self._show_next_frame(frame))

        self._render_frame()

    def _render_frame(self):
        self.start_frame.place(anchor='center', relx=0.5, rely=0.5, relwidth=1, relheight=1)
        self.start_label.place(anchor=CENTER, relx=0.5, rely=0.1)
        self.start_button.place(anchor=CENTER, relx=0.5, rely=0.5)

    @staticmethod
    def _show_next_frame(frame):
        play_audio_thread('sounds/button_click.wav')
        frame.tkraise()
