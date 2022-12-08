import numpy as np
import pdb

def w_vector(k, n, N):
    return np.cos(-2*np.pi*k*n/N) - 1j*np.sin(-2*np.pi*k*n/N)

def w_matrix(N):
    test = np.zeros(shape=[N, N])
    iter_k = np.linspace(0, N-1, N)
    iter_n = iter_k * -2*np.pi/N
    k_mat = np.reshape(np.tile(iter_k, N), [len(iter_k), N]).T
    test = iter_n * k_mat
    dft_matrix = np.cos(test) - 1j*np.sin(test)
    return dft_matrix