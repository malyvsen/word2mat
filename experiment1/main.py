import random
import numpy as np
from matplotlib import pyplot as plt
from tqdm.auto import tqdm

# test matrices of size 8 and 16
# average sentence length in English is 15 to 20. Here we test 0-30 with histogram at every 5 muls

matrix_size = 8
mulsize = 30
eval_interval=5
nb_test=10000
nb_intervals=50
plot_title="unifrom init size 8"

nb_evals=(mulsize//eval_interval)
distribution_values=[[]]*nb_evals
print(distribution_values)
for test in tqdm(range(nb_test), desc="Generating and multiplying matrices", total=nb_test):
    eval = 0
    uniform_matrices = [[[random.random() for e in range(matrix_size)] for e in range(matrix_size)] for e in range(mulsize+1)]
    result_matrix=uniform_matrices[0]
    for j in range(1,mulsize+1):
        result_matrix=np.matmul(result_matrix,uniform_matrices[j])
        if j%eval_interval==0:
            flat_result=np.matrix.flatten(result_matrix)
            if test==0:
                distribution_values[eval]=flat_result
            else:
                distribution_values[eval]=np.append(distribution_values[eval],flat_result)
            eval+=1

for eval in range(nb_evals):
    mean = np.mean(distribution_values[eval])
    max = np.amax(distribution_values[eval])
    min = np.amin(distribution_values[eval])
    intervals=[]
    print(distribution_values)
    print(len(distribution_values[eval]))
    for i in range(nb_intervals):
        intervals.append(min+i*(max-min)/(nb_intervals-1))
    plt.hist(distribution_values[eval],bins=100)
    multiplic_nb=eval_interval+eval*eval_interval
    plt.title(plot_title+" @multiplication "+str(multiplic_nb))
    plt.show()