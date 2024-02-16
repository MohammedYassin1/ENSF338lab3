import random
import timeit
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(10000)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

def quick_sort(arr,low,high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index)
        quick_sort(arr, pivot_index + 1,high)

def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while right > low and arr[right] >= pivot:
            right = right - 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right] ,arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right

def generate_test_case_bub(size, case):
    if case == "best":
        return list(range(1, size + 1))
    elif case == "worst":
        return list(range(size, 0, -1))
    elif case == "average":
        return random.sample(range(1, size + 1), size)

def generate_test_case_qui(size, case):
    if case == "best":
        return list(range(1, size + 1))
    elif case == "worst":
        return list(range(size, 0, -1))
    elif case == "average":
        return random.sample(range(1, size + 1), size)

def plot_performance(test_sizes, results, title):
    plt.figure(figsize=(10, 6))
    for algorithm, times in results.items():
        plt.plot(test_sizes, times, label=algorithm)
    plt.title(title)
    plt.xlabel('Input Size')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Test cases for input sizes
test_sizes = [10, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000]

# Perform tests for each scenario (best, worst, and average) for both algorithms
bub_results = {"best":[], "worst":[], "average": []}
qui_results = {"best":[], "worst":[], "average": []}
for size in test_sizes:
    for case in ["best", "worst", "average"]:
        test_array = generate_test_case_bub(size, case)
        bubble_time = timeit.timeit(lambda: bubble_sort(test_array),number=1)

        test_array = generate_test_case_qui(size, case)
        quick_time = timeit.timeit(lambda: quick_sort(test_array,0,len(test_array) - 1),number=1)

        bub_results[case].append(bubble_time)
        qui_results[case].append(quick_time)

# Plot performance for all scenarios

plt.figure(figsize=(10, 6))

plt.plot(test_sizes, qui_results["best"], label="Quick Sort Best")
plt.plot(test_sizes, qui_results["worst"], label="Quick Sort Worst")
plt.plot(test_sizes, qui_results["average"], label="Quick Sort Average")

plt.plot(test_sizes, bub_results["best"], label="Bubble Sort Best")
plt.plot(test_sizes, bub_results["worst"], label="Bubble Sort Worst")
plt.plot(test_sizes, bub_results["average"], label="Bubble Sort Average")

plt.title("Performance Comparison of Bubble Sort and Quick Sort")
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.legend()
plt.grid(True)
plt.show()