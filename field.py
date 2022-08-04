
"""Выводит в консоль игровое поле"""
def show_field() -> str:
    players = ('player 1', 'player 2')
    symbol = ('X', 'O')
    """Добавляет вертикальные линии"""
    vertical_line = '|'.join([' '*3]*3)
    """Добавляет горизонтальные линии"""
    horiz_line = '|'.join(['—'*3]*3)

    """Перебор длины вертикальных линии"""
    for i in range(len(vertical_line)):
        if i > 1:
            break
        else:
            print(vertical_line, horiz_line, sep = '\n')
            print(vertical_line)


show_field()
