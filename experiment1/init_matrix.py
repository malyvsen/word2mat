import random
import numpy as np
import scipy.stats
import math
random.seed(400)



def uniform_init(dim: int):
    return [[(random.random()-0.5)*np.sqrt(12/dim) for e in range(dim)] for e in range(dim)]

def biased_uniform_init(dim: int):
    return [[random.random()*np.sqrt(12/dim) for e in range(dim)] for e in range(dim)]


def gaussian_init(dim: int):
    return [[np.random.normal() for e in range(dim)] for e in range(dim)]

def cosine_init(dim: int):
    print(scipy.stats.cosine.rvs(loc=0, scale=1 / np.sqrt(dim), size=(dim, dim)))
    return scipy.stats.cosine.rvs(loc=0, scale=1 / np.sqrt(dim), size=(dim, dim))

def xavier_init(dim: int):
    sigma=1/np.sqrt(dim)
    return [[np.random.normal(0,sigma) for e in range(dim)] for e in range(dim)]

def adjusted_xavier_init(dim: int):
    sigma=1/(dim)
    return [[np.random.normal(0,sigma) for e in range(dim)] for e in range(dim)]

def log_normal_init(dim:int):
    sigma=1/np.sqrt(dim)
    return [[np.random.lognormal(0,sigma) for e in range(dim)] for e in range(dim)]


def sym_log_normal_init(dim:int):
    sigma=1/np.sqrt(dim)
    return [[sym_lognorm_val(sigma) for e in range(dim)] for e in range(dim)]

def sym_lognorm_val(sigma):
    rand=random.random()
    if rand > 0.5:
        return np.random.lognormal(0, sigma)
    else:
        return -np.random.lognormal(0, sigma)

def trinary_init(dim:int):
    return [[trin_sample() for e in range(dim)] for e in range(dim)]


def trin_sample():
    rand = random.random()
    if rand > 0.5:
        rand2 = random.random()
        if rand2 > 0.5:
            return 1
        else:
            return -1
    else:
        return 0

