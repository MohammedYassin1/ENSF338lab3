# Exercise 3
# Question 2
def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0

    for i in range(n):
        # Last i elements are already sorted, so no need to check them
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1

    return comparisons, swaps

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
comparisons, swaps = bubble_sort(arr.copy())

print("Sorted array:", arr)
print("Number of comparisons:", comparisons)
print("Number of swaps:", swaps)



# Question 3 (How to test the bubble sort implementation on inputs of increasing size for average-case complexity analysis)
import random

def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

def generate_semi_sorted_array(size):
    return list(range(1, size + 1)) + [random.randint(1, 1000) for _ in range(size // 10)]

for size in [10, 50, 100, 200, 500, 1000]:
    random_array = generate_random_array(size)
    semi_sorted_array = generate_semi_sorted_array(size)

    # Test with random array
    comparisons, swaps = bubble_sort(random_array.copy())
    print(f"Random Array (Size {size}): Comparisons: {comparisons}, Swaps: {swaps}")

    # Test with semi-sorted array
    comparisons, swaps = bubble_sort(semi_sorted_array.copy())
    print(f"Semi-sorted Array (Size {size}): Comparisons: {comparisons}, Swaps: {swaps}")

    print("----")
