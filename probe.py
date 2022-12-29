import time

import simple_draw as sd

sd.resolution = (600, 600)
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

y = 0
x = 0

for j in range(13):
    for i in range(7):
        time.sleep(0.01)
        if (j % 2) == 0:
            point_x = sd.get_point(x + i * 100, y + j * 50)
            point_y = sd.get_point(x + 100 + i * 100, y + 50 + j * 50)
            sd.rectangle(point_x, point_y, color=sd.COLOR_ORANGE, width=1)
        else:
            point_x = sd.get_point(x + i * 100 - 50, y + j * 50)
            point_y = sd.get_point(x + 50 + i * 100, y + 50 + j * 50)
            sd.rectangle(point_x, point_y, color=sd.COLOR_ORANGE, width=1)

sd.pause()
