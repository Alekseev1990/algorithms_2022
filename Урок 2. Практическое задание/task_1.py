"""
Задание 1.	Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ

Решите через рекурсию. Решение через цикл не принимается.

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""

def calculate():
    s = input("Введите операцию (+, -, *, / или 0 для выхода): ")
    if s not in ('+', '-', '*', '/', '0'):
        print("Неизвестная операция"), calculate()
    elif s == '0':
        print("Вы вышли из калькулятора")
    else:
        a = input()
        b = input()
        if a.isdigit() and b.isdigit():
            a = int(a)
            b = int(b)
            if s == '+':
                print(f'Ваш результат {a + b}'), calculate()
            elif s == '-':
                print(f'Ваш результат {a - b}'), calculate()
            elif s == '*':
                print(f'Ваш результат {a * b}'), calculate()
            elif s == '/' and b != 0:
                print(f'Ваш результат {a / b}'), calculate()
            else:
                print("На 0 делть нельзя"), calculate()
        else:
            print("Введите число")
            return calculate()


print(calculate())
