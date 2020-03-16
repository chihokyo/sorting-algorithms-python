"""
快速排序思路1
"""
def quick_sort(arr, low, high):
    if low > high:
        return
    pivot = arr[high]
    left = low
    right = high
    while left < right:
        while left < right and arr[left] < pivot:
            left += 1
        arr[right] = arr[left]
        while left < right and arr[right] >= pivot:
            right -= 1
        arr[left] = arr[right]

        arr[right] = pivot

    quick_sort(arr, low, left - 1)
    quick_sort(arr, right + 1, high)


arr = [ 12, 34, 54, 2, 3, -1, 0, -16]   
quick_sort(arr,0,len(arr)-1)  
print(arr)


"""
快速排序思路2
拆分实现
"""
# 得到pivot基准值index
def partition(arr, left, right):
    pivot = arr[left]
    while left < right:
        while left < right and arr[right] >= pivot:
            right -= 1
        arr[left] = arr[right]
        while left < right and arr[left] < pivot:
            left += 1
        arr[right] = arr[left]
    arr[left] = pivot
    return left

# 快速排序
def quick_sort_part(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)

arr = [ 12, 34, 54, 2, 3, -1, 0, -16] 
quick_sort_part(arr,0,len(arr)-1)  
print(arr)

# result
# [-16, -1, 0, 2, 3, 12, 34, 54]
# [-16, -1, 0, 2, 3, 12, 34, 54]
