from main import HELP

# ИСПРАВИТЬ: если переносите сюда функцию, то переносите и глобальные переменные, которые она использует
new_help = HELP

def show_help() -> None:
    """Выводит в stdout раздел помощи."""
    print(new_help)


# ИСПРАВИТЬ: после проведения теста этот вызов функции нужно закомментировать или удалить
show_help()
