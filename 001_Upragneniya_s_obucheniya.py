# Упражнения по теме:
# Управляющие конструкции ходом выполнения программ в Python

# 1. Дано два числа. Вывести на экран наибольшее из чисел;
a = 6
b = 8
if a > b:
    print(a)
else:
    print(b)

# 2. Пользователь вводит два числа с клавиатуры.
# Вывести на экран yes, если они отличаются друг от друга на 135, иначе вывести на экран No;
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
if abs(a-b) == 135:
    print('yes')
else:
    print('No')

# 3. Дано число. Если оно больше 100 или меньше -100, то вывести на экран символ —,
# иначе вывести на экран символ +;
a = 200
if abs(a) > 100:
    print('\u2013')
else:
    print('+')

# 4. Пользователь вводит номер месяца (от 1 до 12).
# Вывести название сезона года на экран (зима, весна, лето, осень);
a = int(input('Введите номер месяца: '))
if a == 1 or a == 2 or a == 12:
    print('зима')
else:
    if 3 <= a <= 5:
        print('весна')
    else:
        if 6 <= a <=8:
            print('лето')
        else:
            if 9 <= a <= 11:
                print('осень')

# 5. Пользователь вводит три числа. Если все числа больше 10, то вывести на экран yes, иначе no;
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
if a > 10 and b > 10 and c > 10:
    print('yes')
else:
    print('no')
