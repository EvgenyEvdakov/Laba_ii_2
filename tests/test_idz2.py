#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import unittest


sys.path.append("../src")
from idz2 import bfs  # Имя файла с исходным кодом: bfs_pathfinding.py


class TestBFS(unittest.TestCase):
    def setUp(self):
        # Лабиринт для тестов
        self.maze = [
            [1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
            [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
            [1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
            [1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        ]

    def test_no_path(self):
        # Тест с недостижимой целью
        start = (0, 0)
        goal = (0, 1)  # Непроходимая точка
        path = bfs(self.maze, start, goal)
        self.assertIsNone(path, "Путь не должен существовать")

    def test_start_equals_goal(self):
        # Тест, где старт и цель совпадают
        start = (0, 0)
        goal = (0, 0)
        path = bfs(self.maze, start, goal)
        self.assertEqual(path, [start], "Путь должен состоять только из стартовой точки")

    def test_single_step_path(self):
        # Тест с путём из одного шага
        start = (0, 0)
        goal = (1, 0)
        path = bfs(self.maze, start, goal)
        self.assertEqual(path, [start, goal], "Путь должен состоять из двух точек")


if __name__ == "__main__":
    unittest.main()
