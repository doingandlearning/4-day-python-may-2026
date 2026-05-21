import time
from multiprocessing import Pool


def analyse_batch(args):
    batch_id, readings = args
    print(f"Batch {batch_id} starting")
    total = sum(x ** 2 for x in readings)
    print(f"Batch {batch_id} finished, result={total}")
    return (batch_id, total)

# batches = {
#     "alpha": range(1, 50_000_000),
#     "beta": range(1, 50_000_000),
#     "gamma": range(1, 50_000_000),
# }

batches = [
    ("alpha", range(1, 5_000_000)),
    ("beta", range(1, 5_000_000)),
    ("gamma", range(1, 5_000_000)),
]


# processes = []
# for batch_id, readings in batches.items():
#     process = Process(target=analyse_batch, args=(batch_id, readings, results))
#     processes.append(process)
#
# for process in processes:
#     process.start()
#
#
# for process in processes:
#     process.join()
start = time.perf_counter()

with Pool(processes=3) as pool:
    results = pool.map(analyse_batch, batches)

print(results)

# while not results.empty():
#     print(results.get())

elapsed = time.perf_counter() - start
print(f"All done in {elapsed:.2f} seconds")
