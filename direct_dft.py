import numpy as np
from test_src import test_signal_one
import pdb
from common import *
import time

def direct_dft_loops(signal):
    # Create an empty N-point array that will store the DFT
    N = len(signal)
    dft = [0]*N

    # Step through the possible frequencies (k) in the given signal
    for k in range(N):
        # Iterate through each point in the signal
        for n, element in enumerate(signal):
            # Each DFT index becomes to summation of the signal
            # decomposed on the current complex exponential
            dft[k] += element * w_vector(k, n, N)
    return dft

def direct_dft_matrices(signal):
    signal = np.array(signal)
    N = len(signal)

    # Compute the N-point DFT matrix
    
    dft_matrix = w_matrix(N)
    # multiply the signal by the DFT matrix to determine the DFT
    dft = dft_matrix@signal
    return dft

if __name__ == "__main__":
    dft = direct_dft_loops(test_signal_one[:1000])
    mat_start = time.perf_counter()
    dft_2 = direct_dft_matrices(test_signal_one[:1000])
    mat_end = time.perf_counter()
    pdb.set_trace()