# Упражнения по теме:
# Пользовательские функции и основы функционального программирования в Python.

# 1. Написать программу (используя слайды лекции с примерами)
# по вызову функции с печатью любой фразы.
def print_message():
    """ Печать любой фразы """
    print('Любая фраза')


print_message()

# 2. Написать программу (используя слайды лекции с примерами) по вызову функции
# с обязательными (закрепленными) параметрами с печатью любой фразы.
def print_message(m):
    """ Печать любой фразы """
    print(m)


print_message('Любая фраза')

# 3. Показать пример программы с функцией в которой параметры установленные
# по умолчанию получают новое значение.
def print_message(m = 'Фраза по умолчанию'):
    """ Печать любой фразы """
    print(m)


print_message()
print_message('Любая фраза')
