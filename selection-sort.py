"""
最经典做法
"""
def selection_sort(arr: list)-> list:
    n = len(arr)
    for i in range(n):
        smallest_index = i 
        for j in range(i + 1, n):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr

arr = [1,3,-9,8,6,17,-6] 
selection_sort(arr)
print(arr)

"""
好理解的做法
分为两步：
1: 查找最小值的index
2: 进行选择交换
"""
# 找最小
def find_smallest_index(arr: list)-> int:
    smallest_index = 0
    smallest_number = arr[0]
    n = len(arr)
    for i in range(1, n):
        if arr[i] < smallest_number:
            smallest_index = i
            smallest_number = arr[i]
    return smallest_index

# 排序
def selection_sort_of_index(arr: list)-> list:
    sorted_list = []
    n = len(arr)
    for i in range(n):
        smallest_index = find_smallest_index(arr)
        sorted_list.append(arr.pop(smallest_index))
    return sorted_list
        
arr = [1,3,-9,8,6,17,-6] 

print(selection_sort_of_index(arr))