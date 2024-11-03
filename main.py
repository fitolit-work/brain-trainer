import tkinter as tk

from frames.players_frame import PlayersFrame
from frames.start_frame import StartFrame
from model import db_func as db
from utils import checks

window = tk.Tk()
window.title("Fill Good")
window.geometry('500x500')
window['cursor'] = 'target'

player_frame = PlayersFrame(window, 'black', '', '')
start_frame = StartFrame(window, 'black', player_frame.players_frame)

db.make_db()


window.mainloop()