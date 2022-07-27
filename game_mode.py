from main import PLAYERS
#from get_player_name import get_player_name
from get_difficultly_level import get_difficultly_level as gdl

def game_mode(mode) -> str:
    """Запрашивает режим для новой партии, добавляет имя бота либо второго
    игрока в глобальную переменную текущих игроков, запрашивает очерёдность ходов."""
    # stdin -> mode
    mode = input('Choose game mode(single or double): ')
    # if mode == 'single':
    #     get_difficulty_level()
    if mode.lower() == 'single':
        gdl()
    # elif mode == 'double':
    #     get_player_name()
    elif mode == 'double':
        #get_player_name()
    who_is_cross = input('who is cross?: ')
    if who_is_cross == PLAYERS['player1']:
        PLAYERS['player2'] == 'O'
    return mode
    # stdin -> who_is_cross
    # name -> PLAYERS
    # return -> mode

game_mode(single)
