import random
import numpy as np
random.seed(400)


def Guassian_sqrt(dim:int):
    return [squared__Gaussian_sample(dim) for e in range(dim)]


def squared__Gaussian_sample(dim:int):
    rand=np.random.normal()/np.sqrt(dim)
    return np.sign(rand)*np.sqrt(np.abs(rand))


