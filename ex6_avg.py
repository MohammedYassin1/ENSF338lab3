# Exercise 6

# Question 1
# Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not in the array

# Example usage:
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
target_value = 6
result = linear_search(my_list, target_value)
print(f"Linear Search: Target {target_value} found at index {result}" if result != -1 else f"Linear Search: Target {target_value} not found")


# Quicksort and Binary Search
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Return the index if the target is found
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Return -1 if the target is not in the array

# Example usage:
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_list = quicksort(my_list)
target_value = 6
result = binary_search(sorted_list, target_value)
print(f"Binary Search: Target {target_value} found at index {result}" if result != -1 else f"Binary Search: Target {target_value} not found")



# Question 2
import time
import random

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
    return quicksort(left) + middle + quicksort(right)

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

# Measure performance on 100 random tasks
num_tasks = 100
array_size = 1000  # You can adjust the size of the array based on your requirements
target_value = random.randint(1, array_size)

total_linear_search_time = 0
total_binary_search_time = 0

for _ in range(num_tasks):
    my_list = random.sample(range(1, array_size + 1), array_size)
    
    # Linear Search
    start_time = time.time()
    linear_search(my_list, target_value)
    total_linear_search_time += time.time() - start_time

    # Binary Search with Quicksort
    start_time = time.time()
    sorted_list = quicksort(my_list)
    binary_search(sorted_list, target_value)
    total_binary_search_time += time.time() - start_time

# Calculate average time
avg_linear_search_time = total_linear_search_time / num_tasks
avg_binary_search_time = total_binary_search_time / num_tasks

print(f"Average Linear Search Time: {avg_linear_search_time:.6f} seconds")
print(f"Average Binary Search Time (with Quicksort): {avg_binary_search_time:.6f} seconds")



# Question 3
import time
import random

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
    return quicksort(left) + middle + quicksort(right)

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

input_sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
num_tasks = 100

for size in input_sizes:
    total_linear_search_time = 0
    total_binary_search_time = 0

    for _ in range(num_tasks):
        my_list = random.sample(range(1, size + 1), size)
        
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

    print(f"Input Size: {size}\n"
          f"Average Linear Search Time: {avg_linear_search_time:.6f} seconds\n"
          f"Average Binary Search Time (with Quicksort): {avg_binary_search_time:.6f} seconds\n"
          "--------------------------------------")




# Question 4 (Plots the performance of both alogirthms)
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
    return quicksort(left) + middle + quicksort(right)

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
            my_list = random.sample(range(1, size + 1), size)
            
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
    plt.title('Performance Comparison: Linear Search vs Binary Search with Quicksort')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    input_sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
    num_tasks = 100

    results = measure_performance(input_sizes, num_tasks)
    plot_results(input_sizes, results)
