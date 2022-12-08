import numpy as np
from common import *
from test_src import *
import pdb

def divide_and_conquer_loops(signal):
    M = len(signal)//4
    L = 4
    N = len(signal)
    if M*L != N:
        raise ValueError('Signal can not be split into MxN array!')
    signal_2d = np.reshape(signal, [M, L]).T

    f = np.empty(shape=[L, M], dtype=np.complex128)
    for index, row in enumerate(signal_2d):
        f[index] = row@w_matrix(M)

    for row_num, row in enumerate(f):
        for col_num, value in enumerate(row):
            f[row_num, col_num] = w_vector(row_num*col_num, 1, N)*value
    
    for col_num in range(len(f[0])):
        f[:, col_num] = f[:, col_num]@w_matrix(L)
    
    return np.reshape(f, [M*L])

def radix_two_fft(signal):
    pass

if __name__ == "__main__":
    f = divide_and_conquer_loops(test_signal_one)