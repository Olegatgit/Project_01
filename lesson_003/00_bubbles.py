# -*- coding: utf-8 -*-
# 12345

#987

import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

def buble(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2)


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# for y in range(100, 301, 100):
#     for x in range(100, 1100, 100):
#         point = sd.get_point(x, y)
#         buble(point=point, step=5)


# Нарисовать 10 пузырьков в ряд

# Нарисовать три ряда по 10 пузырьков

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    point = sd.random_point()
    step = random.randint(2, 10)
    buble(point=point, step=step)

sd.pause()
