####
# https://developer.apple.com/forums/thread/695963
# https://github.com/conda-forge/numpy-feedstock/issues/253
####
import time
import numpy as np
np.random.seed(42)
a = np.random.uniform(size=(300, 300))
runtimes = 10

timecosts = []
for _ in range(runtimes):
    s_time = time.time()
    for i in range(100):
        a += 1
        np.linalg.svd(a)
    timecosts.append(time.time() - s_time)

print(f'numpy mean of {runtimes} runs: {np.mean(timecosts):.5f}s')