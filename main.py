import tkinter as tk

from frames.create_player_frame import CreatePlayerFrame
from frames.game_mode import GameModeFrame
from frames.load_player_frame import LoadPlayerFrame
from frames.players_frame import PlayersFrame
from frames.start_frame import StartFrame
from model import db_func as db
from utils.play_sound import play_audio

window = tk.Tk()
window.title("Fill Good")
window.geometry('500x500')
window['cursor'] = 'target'

player = '?'


def update_player(player_data):
    global player
    player = player_data


game_mode_page = GameModeFrame(window, 'black')
create_player_page = CreatePlayerFrame(window, 'black', update_player)
load_player_page = LoadPlayerFrame(window, 'black', update_player)
players_page = PlayersFrame(window, 'black')
start_page = StartFrame(window, 'black')

start_page.next_frame = players_page.players_frame

players_page.load_player_frame = load_player_page.load_player_frame
players_page.create_player_frame = create_player_page.create_player_frame

load_player_page.back_frame_for_button_back = players_page.players_frame
load_player_page.game_mode_frame = game_mode_page.game_mode_frame

create_player_page.back_frame_for_button_back = players_page.players_frame
create_player_page.game_mode_frame = game_mode_page.game_mode_frame

game_mode_page.back_frame_for_button_back = players_page.players_frame

db.make_db()
window.mainloop()
