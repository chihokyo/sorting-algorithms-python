"""
合并2个有序数组
方法1：通用方法
"""
def merge_two_sorted_array(arrA, arrB):
    arrA_index, arrB_index = 0, 0
    sorted_array = []
    while arrA_index < len(arrA) and arrB_index < len(arrB):
        if arrA[arrA_index] < arrB[arrB_index]:
            sorted_array.append(arrA[arrA_index])
            arrA_index += 1
        else:
            sorted_array.append(arrB[arrB_index])
            arrB_index += 1
    while arrA_index < len(arrA):
        sorted_array.append(arrA[arrA_index])
        arrA_index += 1

    while arrB_index < len(arrB):
        sorted_array.append(arrB[arrB_index])
        arrB_index += 1
    return sorted_array

arrA = [ -5, 1, 3, 8, 9]
arrB = [ 0, 3, 9, 16, 33]
print(merge_two_sorted_array(arrA, arrB))

# result
# [-5, 0, 1, 3, 3, 8, 9, 9, 16, 33]

"""
合并2个有序数组
方法1：python切片
"""
def merge_two_sorted_array_slice(arrA, arrB):
    arrA_index, arrB_index = 0, 0
    sorted_array = []
    while arrA_index < len(arrA) and arrB_index < len(arrB):
        if arrA[arrA_index] < arrB[arrB_index]:
            sorted_array.append(arrA[arrA_index])
            arrA_index += 1
        else:
            sorted_array.append(arrB[arrB_index])
            arrB_index += 1
    sorted_array += arrA[arrA_index:]
    sorted_array += arrB[arrB_index:]
    
    return sorted_array

arrA = [ -5, 1, 3, 8, 9]
arrB = [ 0, 3, 9, 16, 33]
print(merge_two_sorted_array_slice(arrA, arrB))

# result
# [-5, 0, 1, 3, 3, 8, 9, 9, 16, 33]

"""
合并排序，递归思想
"""
def merge_sort(arr):
    
    n = len(arr)
    if n <= 1:
        return arr
    mid = n // 2

    arrA = merge_sort(arr[:mid])
    arrB = merge_sort(arr[mid:])
    # 直到这里都是分割

    # 接下来才是比较合并
    arrA_index, arrB_index = 0, 0
    sorted_array = []
    while arrA_index < len(arrA) and arrB_index < len(arrB):
        if arrA[arrA_index] < arrB[arrB_index]:
            sorted_array.append(arrA[arrA_index])
            arrA_index += 1
        else:
            sorted_array.append(arrB[arrB_index])
            arrB_index += 1
    sorted_array += arrA[arrA_index:]
    sorted_array += arrB[arrB_index:]
    
    return sorted_array

arr = [ 12, 34, 54, 2, 3, -1, 0, -16] 
print(merge_sort(arr))

# result
# [-16, -1, 0, 2, 3, 12, 34, 54]