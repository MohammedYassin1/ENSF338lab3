# Exercise 5

# Question 1
# Traditional Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage:
array = [12, 11, 13, 5, 6]
insertion_sort(array)
print("Sorted array using traditional insertion sort:", array)


# Binary Insertion Sort

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        # Find the position where key should be inserted in the sorted part of the array
        left, right = 0, i - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < key:
                left = mid + 1
            else:
                right = mid - 1

        # Shift elements to make space for the key
        for j in range(i - 1, left - 1, -1):
            arr[j + 1] = arr[j]

        # Insert the key in its correct position
        arr[left] = key

# Example usage:
array = [12, 11, 13, 5, 6]
binary_insertion_sort(array)
print("Sorted array using binary insertion sort:", array)




# Question 2
import timeit
import random

def generate_random_array(length):
    return [random.randint(1, 1000) for _ in range(length)]

def measure_time_sorting(algorithm, array):
    setup_code = f"from __main__ import {algorithm}"
    stmt = f"{algorithm}({array})"
    time_taken = timeit.timeit(stmt, setup=setup_code, number=10)
    return time_taken / 10  # Calculate average time over 10 runs

# Test on arrays of increasing lengths
array_lengths = [100, 500, 1000, 2000, 5000]

for length in array_lengths:
    array = generate_random_array(length)

    traditional_time = measure_time_sorting("insertion_sort", array.copy())
    binary_time = measure_time_sorting("binary_insertion_sort", array.copy())

    print(f"Array length: {length}")
    print(f"Traditional Insertion Sort Time: {traditional_time:.6f} seconds")
    print(f"Binary Insertion Sort Time: {binary_time:.6f} seconds")
    print("------------------------------")




# Question 3 (The code works. Tested it in Jupyter Notebooks since it generates plot without having to save multiple files so please ignore the two yellow line errors)
import timeit
import random
import matplotlib.pyplot as plt
import numpy as np

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        left, right = 0, i - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < key:
                left = mid + 1
            else:
                right = mid - 1
        for j in range(i - 1, left - 1, -1):
            arr[j + 1] = arr[j]
        arr[left] = key

def generate_random_array(length):
    return [random.randint(1, 1000) for _ in range(length)]

def measure_time_sorting(algorithm, array):
    setup_code = f"from __main__ import {algorithm}"
    stmt = f"{algorithm}({array})"
    time_taken = timeit.timeit(stmt, setup=setup_code, number=10)
    return time_taken / 10

# Test on arrays of increasing lengths
array_lengths = [100, 500, 1000, 2000, 5000]

traditional_times = []
binary_times = []

for length in array_lengths:
    array = generate_random_array(length)

    traditional_time = measure_time_sorting("insertion_sort", array.copy())
    binary_time = measure_time_sorting("binary_insertion_sort", array.copy())

    traditional_times.append(traditional_time)
    binary_times.append(binary_time)

# Plot the results
plt.plot(array_lengths, traditional_times, marker='o', label='Traditional Insertion Sort')
plt.plot(array_lengths, binary_times, marker='o', label='Binary Insertion Sort')

# Interpolating functions
x_interp = np.linspace(min(array_lengths), max(array_lengths), 100)
y_interp_traditional = np.interp(x_interp, array_lengths, traditional_times)
y_interp_binary = np.interp(x_interp, array_lengths, binary_times)

plt.plot(x_interp, y_interp_traditional, linestyle='--', label='Traditional Insertion Sort (Interpolated)')
plt.plot(x_interp, y_interp_binary, linestyle='--', label='Binary Insertion Sort (Interpolated)')

plt.xlabel('Array Length')
plt.ylabel('Average Time (seconds)')
plt.title('Comparison of Sorting Algorithms')
plt.legend()
plt.show()



"""
Question 4

The results of the experiment may vary based on the specific characteristics of the input data and the efficiency of the implementation. However, we can discuss the general expected behavior.

In general, binary insertion sort is expected to perform better than traditional insertion sort, especially as the size of the array increases. The reason behind this is that binary insertion sort reduces the number of comparisons by using binary search to find the correct position for each element, whereas traditional insertion sort compares each element with every element in the sorted portion of the array.

Binary insertion sort has a time complexity of O(n log(n)) for the comparisons and O(n^2) for the shifting, while traditional insertion sort has a time complexity of O(n^2). However, in practice, the reduced number of comparisons in binary insertion sort often makes it more efficient, especially for large datasets.

In the plotted results, it can be observed that the binary insertion sort has lower average times compared to traditional insertion sort, and the difference may become more pronounced as the array length increases. The interpolated lines help visualize the expected trends based on the available data points.

"""