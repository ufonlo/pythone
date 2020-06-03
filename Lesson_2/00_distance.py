#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pprint import pprint
# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = dict()
moscov = sites['Moscow']
london = sites['London']
paris = sites['Paris']
moscov_london = ((moscov[0] - london[0])**2 + (moscov[1] - london[1]) **2) ** .5
moscov_paris = ((moscov[0] - paris[0])**2 + (moscov[1] - paris[1]) **2) ** .5
paris_london = ((paris[0] - london[0])**2 + (paris[1] - london[1]) **2) ** .5

distances['Moscow'] = {}
distances['Moscow']['London'] = moscov_london
distances['Moscow']['Paris'] = moscov_paris
distances['London'] = {}
distances['London']['Moscow'] = moscov_london
distances['London']['Paris'] = paris_london
distances['Paris'] = {}
distances['Paris']['Moscow'] = moscov_paris
distances['Paris']['London'] = paris_london
pprint(distances)