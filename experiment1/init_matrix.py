import random


def uniform_init(dim: int):
    return [[random.random() for e in range(dim)] for e in range(dim)]