"""
最经典的冒泡做法
"""

def bubble_sort(arr: list) -> list:
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [ 12, 34, 54, 2, 3, -1, 0, -16]  
print(bubble_sort(arr))

# result
# [-16, -1, 0, 2, 3, 12, 34, 54]


"""
小小的优化
如果第一次遍历并没有交换的数字则认为已排序
"""

def opti_bubble_sort(arr: list) -> list:
    n = len(arr)
    for i in range(n):
        count = 0
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count += 1
        if count == 0:
            break
    return arr

arr = [ 12, 34, 54, 2, 3, -1, 0, -16]  
print(opti_bubble_sort(arr))

# result
# [-16, -1, 0, 2, 3, 12, 34, 54]