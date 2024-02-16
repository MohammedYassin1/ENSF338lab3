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
