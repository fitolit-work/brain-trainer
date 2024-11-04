import tkinter as tk

from frames.create_player_frame import CreatePlayerFrame
from frames.load_player_frame import LoadPlayerFrame
from frames.players_frame import PlayersFrame
from frames.start_frame import StartFrame
from model import db_func as db


window = tk.Tk()
window.title("Fill Good")
window.geometry('500x500')
window['cursor'] = 'target'

create_player_frame = CreatePlayerFrame(window, 'black')
load_player_frame = LoadPlayerFrame(window, 'black')
players_frame = PlayersFrame(window, 'black', create_player_frame.create_player_frame,
                             load_player_frame.load_player_frame)
start_frame = StartFrame(window, 'black', players_frame.players_frame)

db.make_db()

window.mainloop()
