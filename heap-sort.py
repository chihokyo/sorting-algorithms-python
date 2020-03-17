"""
堆排序
步骤1 堆化
步骤2 排序
"""

# 堆化
def heapify(arr, n, i):
    largest = i 
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    if lchild < n and arr[lchild] > arr[largest]:
        largest = lchild
    if rchild < n and arr[rchild] > arr[largest]:
        largest = rchild
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, n, largest)

# 排序
def heap_sort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]   
        heapify(arr, i, 0)

arr = [ 12, 34, 54, 2, 3, -1, 0, -16]  
heap_sort(arr)  
print(arr)

# result
# [-16, -1, 0, 2, 3, 12, 34, 54]