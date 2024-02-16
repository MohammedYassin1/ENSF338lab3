def merge_sort(arr,low,high):
    if low<high:
        mid = (low + high)//2
        merge_sort(arr, low,mid)
        merge_sort(arr, mid + 1,high)
        merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    left_array = arr[low:mid+1]
    right_array = arr[mid+1:high+1]


    left_index = 0
    right_index = 0
    merged_index = low


    while left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index] <= right_array[right_index]:
            arr[merged_index] = left_array[left_index]
            left_index += 1
        else:
            arr[merged_index] = right_array[right_index]
            right_index += 1
        merged_index += 1

 
    while left_index < len(left_array):
        arr[merged_index] = left_array[left_index]
        left_index += 1
        merged_index += 1
    
    while right_index < len(right_array):
        arr[merged_index] = right_array[right_index]
        right_index += 1
        merged_index += 1

array = [4,2,1,45,42,3]
merge_sort(array,0,len(array)-1,)
print(array)

""""
2. The worst-case complexity of the overall mergesort algorithm using this merge() function is O(n log n).
This is because the divide step takes O(log n) time as we repeatedly halve the array until reaching arrays of size
1, and the merge step takes O(n) time as we merge the divided arrays.

3.
Initial list: [8, 42, 25, 3, 3, 2, 27, 3]
Split into two halves: [8, 42, 25, 3] and [3, 2, 27, 3]
Split each half again: [8, 42] [25, 3] [3, 2] [27, 3]
Split each half again: [8] [42] [25] [3] [3] [2] [27] [3]

Merge [8] and [42] to get [8, 42]
Merge [25] and [3] to get [3, 25]
Merge [3] and [2] to get [2, 3]
Merge [27] and [3] to get [3, 27]

Merge [8, 42] and [3, 25] to get [3, 8, 25, 42]
Merge [2, 3] and [3, 27] to get [2, 3, 3, 27]
Now merge the remaining two lists [3, 8, 25, 42] and [2, 3, 3, 27]:
Merge [3, 8, 25, 42] and [2, 3, 3, 27] to get [2, 3, 3, 3, 8, 25, 27, 42]
sorted list: [2, 3, 3, 3, 8, 25, 27, 42].

4.The number of steps taken is consistent with our complexity analysis. Each division step halved the size of 
the array until we reached arrays of size 1, which took O(log n) steps, and each merge step combined the divided 
arrays, taking O(n) steps. Thus, the overall time complexity matches our analysis of O(n log n).

"""