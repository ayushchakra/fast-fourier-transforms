import numpy as np
from common import *
from test_src import *

def divide_and_conquer_loops(signal):
    # Split the signal into a LxM matrix
    M = len(signal)//4
    L = 4
    N = len(signal)
    if M*L != N:
        raise ValueError('Signal can not be split into MxN array!')
    signal_2d = np.reshape(signal, [M, L]).T

    # Pre-allocate memory for a LxM complex numpy array to store the FFT
    f = np.empty(shape=[L, M], dtype=np.complex128)

    # Compute the M point DFTs of each row
    for index, row in enumerate(signal_2d):
        f[index] = row@w_matrix(M)

    # Apply a phase factor to each value
    for row_num, row in enumerate(f):
        for col_num, value in enumerate(row):
            f[row_num, col_num] = w_vector(row_num*col_num, 1, N)*value
    
    # Compute the L point DFTs of each column
    for col_num in range(len(f[0])):
        f[:, col_num] = f[:, col_num]@w_matrix(L)
    
    # Return the computed DFT as a 1D ndarray
    return np.reshape(f, [M*L])

def divide_and_conquer_matrices(signal):
    # Split the signal into a LxM matrix
    M = len(signal)//4
    L = 4
    N = len(signal)
    if M*L != N:
        raise ValueError('Signal can not be split into MxN array!')
    signal_2d = np.reshape(signal, [M, L]).T

    # Pre-allocate memory for a LxM complex numpy array to store the FFT
    f = np.empty(shape=[L, M], dtype=np.complex128)

    # Compute the M point DFTs of each row
    for index, row in enumerate(signal_2d):
        f[index] = row@w_matrix(M)

    # Construct a matrix containing each phase factor and apply it (element wise)
    # to the M point DFTs that were calculated
    col_linspace = np.linspace(0, len(f)-1, len(f))
    col_index = np.reshape(np.tile(col_linspace, len(f[0])), (len(f[0]), len(col_linspace))).T
    row_linspace = np.linspace(0, len(f[0])-1, len(f[0]))
    row_index = np.reshape(np.tile(row_linspace, len(f)), (len(f), len(row_linspace)))
    index_product = np.multiply(col_index, row_index)
    phase_factor = np.cos(-2*np.pi*index_product/N) -1j*np.sin(-2*np.pi*index_product/N)
    f = np.multiply(f, phase_factor)
    
    # Compute the L point DFTs of each column
    for col_num in range(len(f[0])):
        f[:, col_num] = f[:, col_num]@w_matrix(L)
    
    # Return the computed DFT as a 1D ndarray
    return np.reshape(f, [M*L])

if __name__ == "__main__":
    f1 = divide_and_conquer_matrices(test_signal_one[:100])
    f2 = divide_and_conquer_loops(test_signal_one[:100])