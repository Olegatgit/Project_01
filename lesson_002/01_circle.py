#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть значение радиуса круга
radius = 42

# Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
# подсказки:
#       формулу можно подсмотреть в интернете,
#       пи возьмите равным 3.1415926
#       точность указывается в функции round()
#
circle_square = round(3.1415926 * radius ** 2, 4)
print('Площадь круга = ', circle_square)

# Далее, пусть есть координаты точки
# point = (23, 34)
point = (30, 30)
# где 23 - координата х, 34 - координата у

# Если точка point лежит внутри того самого круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
# подсказки:
#       нужно определить расстояние от этой точки до начала координат (0, 0)
#       формула так же есть в интернете
#       квадратный корень - это возведение в степень 0.5
#       операции сравнения дают булевы константы True и False

point_distance = round((point[0] ** 2 + point[1] ** 2) ** 0.5, 4)
print('Расстояние = ', point_distance)
diff_value = radius - point_distance
diff_value_bool = bool(diff_value)
#   print(diff_value_bool)
if diff_value < 0:
    print('Точка вне круга')
else:
#   print(diff_value)
    print('Точка внутри круга')

# Аналогично для другой точки
point_2 = (30, 30)
# Если точка point_2 лежит внутри круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
# TODO здесь ваш код

# Пример вывода на консоль:
#
# 77777.7777
# False
# False


