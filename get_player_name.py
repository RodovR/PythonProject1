"""Импорт из модуля main глобальной переменной STATS"""
from main import STATS

"""Запрос имени игрока и передача введённого значения в глобальную переменную STATS"""
def get_player_name(name) -> None:
    """Объявление глобальной переменной STATS в локальной функций get_player_name"""
    global STATS
    new_player = ()
    """Запрашивает имя игрока и проверяет присутствие этого имени в
        глобальной переменной статистики, добавляет имя в глобальную переменную текущих игроков."""
    name = input('Введите имя пользователя: ')
    # if name not in STATS:
    if name not in STATS:
        new_player.append(name)
    """Выход из цикла при условий ввода пустой строки"""
    while name == '':
        break
    #     new_player(name)
    # name -> PLAYERS

#get_player_name()
