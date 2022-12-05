import numpy as np

def w_vector(k, n, N):
    return np.array([np.cos(-2*np.pi*k*n/N), np.sin(-2*np.pi*k*n/N)])

def w_matrix(N):
    test = np.zeros(shape=[N, N])
    iter_k = np.linspace(0, N-1, N)
    iter_n = iter_k * -2*np.pi/N
    for k in iter_k:
        test[:,int(k)] = (k*iter_n).T
    real_dft_matrix = np.cos(test)
    imag_dft_matrix = np.sin(test)
    return real_dft_matrix, imag_dft_matrix