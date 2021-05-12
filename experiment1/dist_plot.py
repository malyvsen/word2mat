from tqdm.auto import tqdm
import numpy as np
from matplotlib import pyplot as plt
import scipy

def plot_eig_magnitudes(nb_test:int, matrix_dim:int,init_func,plot_title:str,nb_intervals:int):
    eigs=[]
    for test in tqdm(range(nb_test), desc="Calculating eigs", total=nb_test):
        matrix = init_func(matrix_dim)
        eigs=np.append(eigs,np.linalg.eig(matrix)[0])
    plt.hist(abs(eigs), bins=nb_intervals)
    plt.title(plot_title + " magnitude of eigenvalues")
    plt.show()


def plot_dist_mul(nb_test: int, matrix_dim: int, init_func, plot_title: str,mulsize:int,
                  eval_interval:int,nb_intervals:int,scale_adjustment=False,sqroot=False):
    nb_evals = (mulsize // eval_interval)+1
    distribution_values = [[]] * nb_evals
    for test in tqdm(range(nb_test), desc="Generating and multiplying matrices", total=nb_test):

        uniform_matrices = [init_func(matrix_dim) for e in range(mulsize + 1)]
        result_matrix = uniform_matrices[0]
        if test == 0:
            distribution_values[0] = result_matrix
        else:
            distribution_values[0] = np.append(distribution_values[0], result_matrix)
        eval = 1
        for j in range(1, mulsize + 1):
            result_matrix = np.matmul(result_matrix, uniform_matrices[j])
            if sqroot:
                result_matrix=np.sqrt(abs(result_matrix))*np.sign(result_matrix)
            if j % eval_interval == 0:
                flat_result = np.matrix.flatten(result_matrix)
                if test == 0:
                    distribution_values[eval] = flat_result
                else:
                    distribution_values[eval] = np.append(distribution_values[eval], flat_result)
                eval += 1
    for eval in range(nb_evals):
        print(scipy.stats.kurtosis(distribution_values[eval]))
        if scale_adjustment:
            mean = np.mean(distribution_values[eval])
            std=np.std(distribution_values[eval])
            nb_stds_each_side=3
            step=nb_stds_each_side*2*std/nb_intervals
            intervals=[]
            for i in range(nb_intervals):
                intervals.append(mean-nb_stds_each_side*std+i*step)
            plt.hist(distribution_values[eval], bins=intervals)
        else:
            plt.hist(distribution_values[eval], bins=nb_intervals)
        multiplic_nb =  eval * eval_interval
        plt.title(plot_title + " @multiplication " + str(multiplic_nb))
        plt.show()
