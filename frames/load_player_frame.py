import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import CENTER

from model.db_func import load_user
from utils import checks
from utils.play_sound import play_audio_thread


class LoadPlayerFrame:
    game_mode_frame: tk.Frame

    def __init__(self, parent, bg, update_player):
        self.update_player = update_player

        self.load_player_frame = tk.Frame(parent, bg=bg)
        self.load_player_title_label = ttk.Label(self.load_player_frame, text='Upload your player', background='black',
                                                 foreground='#4eff00', font=('Lucida Console', 20))
        self.load_player_entry_label = ttk.Label(self.load_player_frame, text='Player name:', background='black',
                                                 foreground='#4eff00', font=('Lucida Console', 14))
        self.load_player_help_label = ttk.Label(self.load_player_frame, text='', background='black',
                                                foreground='red', font=('Lucida Console', 12))

        self.load_player_entry = tk.Entry(self.load_player_frame, background='black',
                                          foreground='#4eff00', bd=5, insertbackground='#4eff00',
                                          font=('Lucida Console', 14))

        self.game_mode_frame = ''
        self.load_player_button = tk.Button(self.load_player_frame, text='Load', font=('Lucida Console', 14),
                                            command=self._load_player)

        self.back_frame_for_button_back = ''
        self.load_player_button_back = tk.Button(self.load_player_frame, text='Back', font=('Lucida Console', 14),
                                                 command=self._load_back_frame)
        self.player = ''

        self._render_frame()

    def _render_frame(self):
        self.load_player_frame.place(anchor='center', relx=0.5, rely=0.5, relwidth=1, relheight=1)
        self.load_player_title_label.place(anchor=CENTER, relx=0.5, rely=0.1)
        self.load_player_entry_label.place(anchor=CENTER, relx=0.5, rely=0.25)
        self.load_player_entry.place(anchor=CENTER, relx=0.5, rely=0.35)
        self.load_player_help_label.place(anchor=CENTER, relx=0.5, rely=0.4)
        self.load_player_button.place(anchor=CENTER, relx=0.5, rely=0.6)
        self.load_player_button_back.place(anchor=CENTER, relx=0.5, rely=0.8)

    def _load_player(self):

        play_audio_thread('sounds/button_click.wav')
        result, success = checks.spaces_in_word(self.load_player_entry.get())
        self.load_player_entry.delete(0, 'end')
        if success:
            self.player = load_user(result.lower())
            print(self.player, '_load_player')
            self.update_player(self.player)
            if self.player:
                if self.game_mode_frame:
                    self.game_mode_frame.tkraise()

                    # изменение имени игрока
                    for widget in self.game_mode_frame.winfo_children():
                        if hasattr(widget, "player_name"):
                            widget['text'] = f'Your Player: {result}'
            else:
                self.load_player_help_label['text'] = "Player is not define! Try again..."
        else:
            self.load_player_help_label['text'] = result
            self.load_player_entry.delete(0, 'end')

    def _load_back_frame(self):
        play_audio_thread('sounds/button_click.wav')
        if self.back_frame_for_button_back:
            self.back_frame_for_button_back.tkraise()

    def get_player(self):
        print(self.player, 'get_player')
        return self.player
