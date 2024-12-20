#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import sys

sys.path.append('../src')
from idz1 import countIslands  # Имя файла с вашим кодом: count_islands.py

class TestCountIslands(unittest.TestCase):
    def test_multiple_islands(self):
        mat = [
            [0, 0, 1, 0, 1, 1, 0, 1, 1, 0],
            [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
            [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0, 1, 1, 0, 0, 1],
            [1, 0, 1, 0, 1, 1, 0, 1, 1, 0],
            [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
            [0, 0, 0, 0, 1, 1, 1, 1, 0, 1],
            [0, 1, 1, 0, 1, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 0, 1, 0]
        ]
        self.assertEqual(countIslands(mat), 3, "Ожидается 3 островов")

    def test_single_island(self):
        mat = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        self.assertEqual(countIslands(mat), 1, "Ожидается 1 остров")

    def test_no_islands(self):
        mat = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.assertEqual(countIslands(mat), 0, "Ожидается 0 островов")

    def test_diagonal_islands(self):
        mat = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]
        self.assertEqual(countIslands(mat), 1, "Ожидается 1 остров")

    def test_empty_matrix(self):
        mat = []
        self.assertEqual(countIslands(mat), 0, "Ожидается 0 островов для пустой матрицы")

if __name__ == "__main__":
    unittest.main()