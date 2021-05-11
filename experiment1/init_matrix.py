import random
import numpy as np
import scipy.stats



def uniform_init(dim: int):
    return [[random.random() for e in range(dim)] for e in range(dim)]

def gaussian_init(dim: int):
    return [[np.random.normal()/3 for e in range(dim)] for e in range(dim)]

def cosine_init(dim: int):
    return scipy.stats.cosine.rvs(loc=0, scale=1 / np.sqrt(dim), size=(dim, dim))

