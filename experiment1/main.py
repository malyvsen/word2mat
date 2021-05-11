import numpy as np
from matplotlib import pyplot as plt
from tqdm.auto import tqdm
import init_matrix
import dist_plot

# test matrices of size 8 and 16
# average sentence length in English is 15 to 20. Here we test 0-30 with histogram at every 5 muls

matrix_dim = 8
mulsize = 30
eval_interval=5
nb_test=10000
nb_intervals=100
plot_title="unifrom init size 16"


dist_plot.plot_eig_magnitudes(nb_test, matrix_dim,init_matrix.uniform_init,plot_title,nb_intervals)
dist_plot.plot_dist_mul(nb_test, matrix_dim, init_matrix.uniform_init, plot_title,mulsize,eval_interval,nb_intervals)
