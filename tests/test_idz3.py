#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import sys

sys.path.append('../src')
from idz3 import Problem, breadth_first_search  # Имя файла с вашим кодом: bfs_graph.py

class TestBreadthFirstSearch(unittest.TestCase):
    def setUp(self):
        # Граф для тестов (список смежности)
        self.graph = {
            1: [(19, 122), (4, 140), (2, 43)],
            2: [(1, 43), (3, 35), (21, 57)],
            3: [(2, 35), (4, 68)],
            4: [(1, 140), (3, 68), (5, 96), (23, 98), (18, 147)],
            5: [(4, 96), (13, 112), (12, 56)],
            18: [(19, 231), (15, 147), (17, 53), (4, 147)],
            19: [(18, 231), (1, 122)],
            12: [(5, 56), (13, 88)],
        }

    def test_shortest_path_found(self):
        start, goal = 18, 12
        problem = Problem(start, goal)
        path, distance = breadth_first_search(problem, self.graph)

        # Проверяем, что найденный путь корректен
        self.assertIsNotNone(path, "Путь должен быть найден")
        self.assertEqual(path[0], start, "Путь должен начинаться с начальной точки")
        self.assertEqual(path[-1], goal, "Путь должен заканчиваться конечной точкой")
        self.assertEqual(distance, 299, "Длина пути должна быть равна ожидаемой")

    def test_no_path(self):
        start, goal = 18, 26  # Между 18 и 26 нет пути в графе
        problem = Problem(start, goal)
        path, distance = breadth_first_search(problem, self.graph)

        # Проверяем, что путь не найден
        self.assertIsNone(path, "Путь не должен быть найден")
        self.assertEqual(distance, float('inf'), "Длина пути должна быть бесконечностью")

    def test_start_is_goal(self):
        start = goal = 18  # Начальная и конечная точка совпадают
        problem = Problem(start, goal)
        path, distance = breadth_first_search(problem, self.graph)

        # Проверяем, что возвращается корректный результат
        self.assertEqual(path, [start], "Путь должен состоять только из начальной точки")
        self.assertEqual(distance, 0, "Длина пути должна быть равна 0")

if __name__ == "__main__":
    unittest.main()