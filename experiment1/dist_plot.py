from tqdm.auto import tqdm
import numpy as np
from matplotlib import pyplot as plt
import scipy


def plot_dist_mul(nb_test: int, matrix_dim: int, init_func, plot_title: str,mulsize:int,
                  eval_interval:int,nb_intervals:int,scale_adjustment=False,sqroot=False):
    nb_evals = (mulsize // eval_interval)+1
    distribution_values = [[]] * nb_evals
    for test in tqdm(range(nb_test), desc="Generating and multiplying vectors", total=nb_test):

        generated_vectors = [init_func(matrix_dim) for e in range(mulsize + 1)]
        result_vector = generated_vectors[0]
        if test == 0:
            distribution_values[0] = result_vector
        else:
            distribution_values[0] = np.append(distribution_values[0], result_vector)
        eval = 1
        for j in range(1, mulsize + 1):
            result_vector = np.multiply(result_vector, generated_vectors[j])
            if sqroot:
                result_vector=np.sqrt(abs(result_vector))*np.sign(result_vector)
            if j % eval_interval == 0:
                flat_result = result_vector
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