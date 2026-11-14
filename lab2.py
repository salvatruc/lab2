# Вводим три числа
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

# Находим максимальное число с помощью условий
if a >= b and a >= c:
    max_num = a
elif b >= a and b >= c:
    max_num = b
else:
    max_num = c

# Находим минимальное число с помощью условий
if a <= b and a <= c:
    min_num = a
elif b <= a and b <= c:
    min_num = b
else:
    min_num = c

# Вычисляем разность максимального и минимального чисел
difference = max_num - min_num

# Выводим результаты на экран
print("Минимальное число:", min_num)
print("Максимальное число:", max_num)
print("Разность:", difference)