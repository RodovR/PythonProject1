from field import show_field

# FIXME: не забудьте аннотировать и документировать функцию
def check_win()->list:
    # Проверяет каждый ряд на выигрышную комбинацию
    for i in range(len(show_field())):
        if show_field()[0] and show_field()[1] and show_field()[2] == 'X' or 'O':
            print('You Win')
        else:
            print('You Lose')

check_win()
