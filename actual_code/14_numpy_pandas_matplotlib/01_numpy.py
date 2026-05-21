import numpy as np

# pandas
# matplotlib

science_results = [45, 30, 65, 52, 31]
maths_results = [33, 45, 23, 63, 54]

maths_tmp = []
for result in maths_results:
    maths_tmp.append(result + 5)

maths_results = np.array(maths_tmp)
science_results = np.array(science_results)
science_results = science_results + 5
science_results += 5
total_results = maths_results + science_results
print(total_results)

import time

start = time.perf_counter()
print(sum([i ** 2 for i in range(50_000_000)]))
end = time.perf_counter() - start
print(end)

print("=" * 100)
start = time.perf_counter()
numbers = np.arange(1, 50_000_000, dtype=np.float64)
numbers **= 2
print(np.sum(numbers))
end = time.perf_counter() - start
print(end)