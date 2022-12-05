import time
from direct_dft import *
from test_src import *

loop_start = time.perf_counter()
dft = direct_dft_loops(test_signal_one[:1000])
loop_end = time.perf_counter()
mat_start = time.perf_counter()
dft_2 = direct_dft_matrices(test_signal_one[:1000])
mat_end = time.perf_counter()