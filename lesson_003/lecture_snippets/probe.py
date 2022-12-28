import random
import time

import simple_draw as sd


# COLOR_RED = (255, 0, 0)
# COLOR_ORANGE = (255, 127, 0)
# COLOR_YELLOW = (255, 255, 0)
# COLOR_GREEN = (0, 255, 0)
# COLOR_CYAN = (0, 255, 255)
# COLOR_BLUE = (0, 0, 255)
# COLOR_PURPLE = (255, 0, 255)
#
# COLOR_SET = [COLOR_PURPLE, COLOR_BLUE, COLOR_CYAN, COLOR_GREEN, COLOR_YELLOW, COLOR_ORANGE, COLOR_RED]

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

sd.resolution = (1200, 600)
# def buble(point, step):
#     radius = 50
#     for _ in range(3):
#         radius += step
#         sd.circle(center_position=point, radius=radius, width=2)
# point = sd.random_point()
# step = random.randint(2, 10)
# buble(point=point, step=step)

# start_x = 0
# end_x = 850
# start_y = -200
# end_y = 700
# line_width = 50
#
# for i in range(7):
#
#     s_point = sd.get_point(start_x + line_width * i, start_y)
#     e_point = sd.get_point(end_x + line_width * i, end_y)
#     sd.line(start_point=s_point, end_point=e_point, color=rainbow_colors[i], width=line_width)
#     # time.sleep(.2)
#
#
# sd.pause()
# sd.quit()

start_x = 0
end_x = 850
start_y = -200
end_y = 700
line_width = 50

for i in range(7):

    s_point = sd.get_point(600, - 300)
    sd.circle(s_point, radius=600 + i * line_width, color=rainbow_colors[i], width=line_width)
    # sd.line(start_point=s_point, end_point=e_point, color=rainbow_colors[i], width=line_width)
    # time.sleep(.2)


sd.pause()
#123445 12345
#321
