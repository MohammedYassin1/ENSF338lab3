import matplotlib.pyplot as plt
import timeit
import json
import sys
sys.setrecursionlimit(10000)


with open("ex7data.json", 'r') as file:
    arr = json.load(file)

with open("ex7tasks.json", 'r') as file:
    targets = json.load(file)


final = {}

def binary_search_with_initial_midpoint(target, arr, low, high, initial_mid = None):
    if low <= high:
        mid = initial_mid
        if initial_mid == None:
            mid = ((low + high) // 2)

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_with_initial_midpoint(target, arr, mid + 1, high)  
        else:
            return binary_search_with_initial_midpoint(target, arr, low, mid - 1)   
    return -1

def main():
    for target in targets:
        results = {}
        midpoint = 1
        best_Mid = 1
        while(midpoint < len(arr)):
            time_taken = timeit.timeit(lambda: binary_search_with_initial_midpoint(target,arr,0, len(arr), midpoint),number=1)
            results[midpoint] = time_taken
            if results[midpoint] <= results[best_Mid]:
                best_Mid = midpoint 
            midpoint = midpoint + 1000
        final[target] = best_Mid

    print(final)
        
    plt.scatter(final.keys(), final.values())
    plt.xlabel('targets')
    plt.ylabel('Midpoints')
    plt.title('Performance of Binary Search with Different Initial Midpoints')
    plt.show() 


main()


"""
4. The choice of midpoint does affect the preformance. This is because if the chosen midpoint is equal to the target then no 
recursive calls are made.This is directly reflected in the graph, which has a roughly linear relationship which would be even 
more well defined if we tested all possible initial midpoints.  

"""