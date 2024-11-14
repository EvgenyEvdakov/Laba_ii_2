#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import deque

class Node:
    def __init__(self, state, parent=None):
        self.state = state  # текущий город/узел
        self.parent = parent  # предыдущий узел в пути

    def path(self):
        # Восстанавливает путь, идя от конечного узла к начальному
        node, path_back = self, []
        while node:
            path_back.append(node.state)
            node = node.parent
        return path_back[::-1]  # Путь в прямом порядке

class FIFOQueue:
    def __init__(self, initial=None):
        self.queue = deque(initial) if initial else deque()

    def pop(self):
        return self.queue.popleft() if self.queue else None

    def appendleft(self, item):
        self.queue.append(item)

    def __bool__(self):
        return len(self.queue) > 0

def expand(graph, node):
    """Генерирует дочерние узлы для текущего узла."""
    for neighbor, _ in graph.get(node.state, []):
        yield Node(neighbor, node)

class Problem:
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal

    def is_goal(self, state):
        return state == self.goal

failure = None  # Значение для обозначения неудачи

def breadth_first_search(problem, graph):
    node = Node(problem.initial)
    if problem.is_goal(node.state):
        return node.path(), 0  # Если начальная точка уже является целью

    frontier = FIFOQueue([node])
    reached = {problem.initial: 0}  # Хранит минимальные расстояния до узлов

    while frontier:
        node = frontier.pop()
        current_distance = reached[node.state]

        for child in expand(graph, node):
            s = child.state
            if problem.is_goal(s):
                # Вычисление общей стоимости пути
                total_distance = current_distance + next(weight for neighbor, weight in graph[node.state] if neighbor == s)
                return child.path(), total_distance

            # Добавляем в очередь только непосещенные или если найден более короткий путь
            if s not in reached:
                edge_weight = next(weight for neighbor, weight in graph[node.state] if neighbor == s)
                reached[s] = current_distance + edge_weight
                frontier.appendleft(child)

    return failure, float('inf')  # если пути не существует

# Пример использования
if __name__ == "__main__":
    # Граф представлен в виде списка смежности
    graph = {
        1: [(19, 122), (4, 140), (2, 43)],
        2: [(1, 43), (3, 35), (21, 57)],
        3: [(2, 35), (4, 68)],
        4: [(1, 140), (3, 68), (5, 96), (23, 98), (18, 147)],
        5: [(4, 96), (13, 112), (12, 56)],
        6: [(5, 76), (10, 46), (7, 32)],
        7: [(6, 32), (8, 72)],
        8: [(7, 72), (9, 80)],
        9: [(8, 80), (11, 50)],
        10: [(6, 46)],
        11: [(9, 50), (24, 56)],
        12: [(5, 56), (13, 88)],
        13: [(12, 88), (14, 35), (5, 112)],
        14: [(13, 35), (25, 54)],
        15: [(18, 147), (4, 24)],
        16: [(17, 38)],
        17: [(18, 53), (16, 38)],
        18: [(19, 231), (15, 147), (17, 53), (4, 147)],
        19: [(18, 231), (1, 122)],
        20: [(1, 57)],
        21: [(2, 57), (22, 67)],
        22: [(21, 67), (24, 56), (23, 82)],
        23: [(4, 98), (22, 82)],
        24: [(22, 56), (11, 56), (27, 40)],
        25: [(14, 54), (26, 46)],
        26: [(25, 46)],
        27: [(24, 40), (28, 57)],
        28: [(27, 57)]
    }

    # Задача: найти кратчайший путь от узла 1 до узла 14
    start = 18
    goal = 12
    problem = Problem(start, goal)
    path, distance = breadth_first_search(problem, graph)
    print("Кратчайший путь:", path)
    print("Длина пути:", distance)
