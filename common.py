import numpy as np

def w_vector(k, n, N):
    return np.array([np.cos(-2*np.pi*k*n/N), np.sin(-2*np.pi*k*n/N)])