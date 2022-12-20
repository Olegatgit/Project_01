#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов
from pprint import pprint

cities = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}

moscow = cities['Moscow']
london = cities['London']
paris = cities['Paris']
moscow_london = round(((moscow[0] - london[0])**2 + (moscow[1] - london[1])**2) ** .5, 1)
moscow_paris = round(((moscow[0] - paris[0])**2 + (moscow[1] - paris[1])**2) ** .5, 1)

distances['Moscow'] = {}
distances['Moscow']['London'] = moscow_london
distances['Moscow']['Paris'] = moscow_paris

print(distances['Moscow']['London'])




