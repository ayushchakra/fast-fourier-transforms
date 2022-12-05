import numpy as np
import pdb

def w_vector(k, n, N):
    return np.array([np.cos(-2*np.pi*k*n/N), np.sin(-2*np.pi*k*n/N)])

def w_matrix(N):
    test = np.zeros(shape=[N, N])
    iter_k = np.linspace(0, N-1, N)
    iter_n = iter_k * -2*np.pi/N
    k_mat = np.reshape(np.tile(iter_k, N), [len(iter_k), N]).T
    test = iter_n * k_mat
    real_dft_matrix = np.cos(test)
    imag_dft_matrix = np.sin(test)
    return real_dft_matrix, imag_dft_matrix