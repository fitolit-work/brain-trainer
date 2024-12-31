import tkinter as tk

from frames.math_game_frame import MathGameFrame
from frames.math_mode_difficulty_frame import MathModeDifficultyFrame
from frames.create_player_frame import CreatePlayerFrame
from frames.game_mode_frame import GameModeFrame
from frames.load_player_frame import LoadPlayerFrame
from frames.players_frame import PlayersFrame
from frames.start_frame import StartFrame
from model import db_func as db

window = tk.Tk()
window.title("Fill Good")
window.geometry('500x500')
window['cursor'] = 'target'

player = '?'
difficulty = {'min_number':1, 'max_number':10, 'point':1}


def update_player(player_data):
    global player
    player = player_data


def update_difficulty(difficulty_data):
    global difficulty
    difficulty = difficulty_data

def get_data():
    global difficulty, player
    return difficulty, player


math_game_page = MathGameFrame(window, 'black', get_data)
math_mode_difficulty_page = MathModeDifficultyFrame(window, 'black', update_difficulty)
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
game_mode_page.math_frame_for_button_mode_math = math_mode_difficulty_page.math_mode_difficulty_frame

math_mode_difficulty_page.back_frame_for_button_back = game_mode_page.game_mode_frame
math_mode_difficulty_page.math_game_frame_for_buttons = math_game_page.math_game_frame

math_game_page.back_frame_for_button_back = game_mode_page.game_mode_frame

db.make_db()
window.mainloop()
