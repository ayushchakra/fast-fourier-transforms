import time
from direct_dft import *
from fft import *
from test_src import *

TEST_SIGNAL_ONE = test_signal_one
TEST_SIGNAL_TWO = test_signal_one[:1000]

def test_dft_loops(signal):
    start = time.perf_counter()
    dft = direct_dft_loops(signal)
    end = time.perf_counter()
    return end - start

def test_dft_matrices(signal):
    start = time.perf_counter()
    dft = direct_dft_matrices(signal)
    end = time.perf_counter()
    return end - start

def test_divide_and_conquer_loops(signal):
    start = time.perf_counter()
    dft = divide_and_conquer_loops(signal)
    end = time.perf_counter()
    return end - start

def test_divide_and_conquer_matrices(signal):
    start = time.perf_counter()
    dft = divide_and_conquer_matrices(signal)
    end = time.perf_counter()
    return end - start

def run_tests(test_signal):
    dft_loop_perf_time = test_dft_loops(test_signal)
    print(f"Looped DFT Performance: {dft_loop_perf_time}s")
    dft_mat_perf_time = test_dft_matrices(test_signal)
    print(f"Matrix DFT Performance: {dft_mat_perf_time}s")
    fft_loop_perf_time = test_divide_and_conquer_loops(test_signal)
    print(f"Looped FFT Performance: {fft_loop_perf_time}s")
    fft_mat_perf_time = test_divide_and_conquer_matrices(test_signal)
    print(f"Matrix FFT Performance: {fft_mat_perf_time}s")

if __name__ == "__main__":
    run_tests(TEST_SIGNAL_TWO)