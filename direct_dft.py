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
    real_dft_matrix, imag_dft_matrix = w_matrix(N)
    real_dft = real_dft_matrix@signal
    imag_dft = imag_dft_matrix@signal
    return np.dstack((real_dft, imag_dft))

if __name__ == "__main__":
    loop_start = time.perf_counter()
    dft = direct_dft_loops(test_signal_one[:1000])
    loop_end = time.perf_counter()
    mat_start = time.perf_counter()
    dft_2 = direct_dft_matrices(test_signal_one[:1000])
    mat_end = time.perf_counter()
    pdb.set_trace()