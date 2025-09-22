import time
import random
import tracemalloc
import matplotlib.pyplot as plt

# Quick Sort 
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Merge Sort 
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

# Merge helper function 
def merge(left, right):
    result = []
    i = j = 0
    # Two sorted arrays merged into one
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Appending any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Measuring time and memory for a sorting function
def assess_performance(sorting_function, input_array):
    tracemalloc.start()  # Tracking memory
    start_time = time.perf_counter()  # Tracking timing
    sorting_function(input_array.copy())  # 
    end_time = time.perf_counter()  # End time
    current_mem, peak_mem = tracemalloc.get_traced_memory()  # Getting memory usage
    tracemalloc.stop()  # Stopping memory tracking
    return end_time - start_time, peak_mem / 1024  # Returns time (s), memory (KB)

# Input sizes for testing
input_sizes = [2000, 4000, 6000, 8000, 10000 ]

# Generating different types of datasets
dataset_variants = {
    "Random": [random.sample(range(10000), size) for size in input_sizes],  # Random order
    "Sorted": [list(range(size)) for size in input_sizes],                 # Already sorted
    "Reverse": [list(range(size, 0, -1)) for size in input_sizes]          # Reverse sorted
}

# Dictionary to store performance data
results = {
    "Quick Sort": {"Random": [], "Sorted": [], "Reverse": []},
    "Merge Sort": {"Random": [], "Sorted": [], "Reverse": []}
}

# Running performance tests for each sorting function and dataset type
for data_label, data_lists in dataset_variants.items():
    for data in data_lists:
        
        # Testing quick_sort
        time_qs, memory_qs = assess_performance(quick_sort, data)
        results["Quick Sort"][data_label].append((time_qs, memory_qs))
        
        # Testing merge_sort
        time_ms, memory_ms = assess_performance(merge_sort, data)
        results["Merge Sort"][data_label].append((time_ms, memory_ms))

# Printing the collected performance results
for algorithm in results:
    print(f"\n--- {algorithm} ---")
    for variant in results[algorithm]:
        print(f"{variant}:")
        for idx, size in enumerate(input_sizes):
            duration, memory_used = results[algorithm][variant][idx]
            print(f"  Size: {size}, Time: {duration:.4f}s, Memory: {memory_used:.2f}KB")
