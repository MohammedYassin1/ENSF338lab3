# Exercise 6
# Question 5
# To demonstrate the worst-case performance of quicksort, we can use an input array that is already sorted in reverse order. In this case, quicksort will have to make ,many comparisons and swaps, resulting in a worst-case scenario.

import time
import random
import matplotlib.pyplot as plt

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(right) + middle + quicksort(left)  # Reverse the ordering

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def measure_performance(input_sizes, num_tasks):
    results = {'Linear Search': [], 'Binary Search (Quicksort)': []}

    for size in input_sizes:
        total_linear_search_time = 0
        total_binary_search_time = 0

        for _ in range(num_tasks):
            my_list = list(range(size, 0, -1))  # Reversed sorted array
            
            # Linear Search
            start_time = time.time()
            linear_search(my_list, random.randint(1, size))
            total_linear_search_time += time.time() - start_time

            # Binary Search with Quicksort
            start_time = time.time()
            sorted_list = quicksort(my_list)
            binary_search(sorted_list, random.randint(1, size))
            total_binary_search_time += time.time() - start_time

        avg_linear_search_time = total_linear_search_time / num_tasks
        avg_binary_search_time = total_binary_search_time / num_tasks

        results['Linear Search'].append(avg_linear_search_time)
        results['Binary Search (Quicksort)'].append(avg_binary_search_time)

    return results

def plot_results(input_sizes, results):
    plt.plot(input_sizes, results['Linear Search'], label='Linear Search')
    plt.plot(input_sizes, results['Binary Search (Quicksort)'], label='Binary Search (Quicksort)')
    plt.xlabel('Input Size')
    plt.ylabel('Average Time (seconds)')
    plt.title('Worst-case Performance: Linear Search vs Binary Search with Quicksort')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    input_sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
    num_tasks = 100

    results = measure_performance(input_sizes, num_tasks)
    plot_results(input_sizes, results)

