import numpy as np
from matplotlib import pyplot as plt
from tqdm.auto import tqdm
import init_vector
import dist_plot
# test matrices of size 8 and 16
# average sentence length in English is 15 to 20. Here we test 0-30 with histogram at every 5 muls

vector_dim = 16*16
mulsize = 30
eval_interval=5
nb_test=100
nb_intervals=100
plot_title="Vector signed sqrt init with square root size 8"
init_func=init_vector.Guassian_sqrt
adjust_scale=True
sqroot=True

# dist_plot.plot_eig_magnitudes(nb_test, matrix_dim,init_func,plot_title,nb_intervals)
dist_plot.plot_dist_mul(nb_test, vector_dim, init_func, plot_title,mulsize,eval_interval,nb_intervals,adjust_scale,sqroot)


