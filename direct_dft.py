import numpy as np
from test_src import test_signal_one
import pdb
from common import *
import time

def direct_dft_loops(signal):
    N = len(signal)
    dft = [0]*N

    for k in range(N):
        for n, element in enumerate(signal):
            dft[k] += element * w_vector(k, n, N)
    return dft

def direct_dft_matrices(signal):
    signal = np.array(signal)
    N = len(signal)
    dft_matrix = w_matrix(N)
    dft = dft_matrix@signal
    return dft

if __name__ == "__main__":
    dft = direct_dft_loops(test_signal_one[:1000])
    mat_start = time.perf_counter()
    dft_2 = direct_dft_matrices(test_signal_one[:1000])
    mat_end = time.perf_counter()
    pdb.set_trace()