import numpy as np
from test_src import test_signal_one
import pdb
from common import *

def w_vector(k, n, N):
    return np.array([np.cos(-2*np.pi*k*n/N), np.sin(-2*np.pi*k*n/N)])

def direct_dft_loops(signal):
    N = len(signal)
    dft = [0]*N

    for k in range(N):
        print(k)
        for n, element in enumerate(signal):
            dft[k] += element * w_vector(k, n, N)
    return dft

if __name__ == "__main__":
    dft = direct_dft_loops(test_signal_one[:100])
    pdb.set_trace()