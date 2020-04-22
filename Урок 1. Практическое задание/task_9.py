"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""

NUMB_1 = int(input("Введите первое число: "))
NUMB_2 = int(input("Введите второе число: "))
NUMB_3 = int(input("Введите третье число: "))

if NUMB_1 == NUMB_2 or NUMB_2 == NUMB_3 or NUMB_1 == NUMB_3:
    print("Все три числа должны быть разными")
elif NUMB_1 < NUMB_2 < NUMB_3 or NUMB_3 < NUMB_2 < NUMB_1:
    print(f"Среднее число: {NUMB_2}")
elif NUMB_2 < NUMB_1 < NUMB_3 or NUMB_3 < NUMB_1 < NUMB_2:
    print(f"Среднее число: {NUMB_1}")
else:
    print(f"Среднее число: {NUMB_3}")

# при использовании функций max() и min() можем получить решение без ветвления - одной строкой
# но решил использовать встроенные функции по минимуму как сказано в условиях задачи
