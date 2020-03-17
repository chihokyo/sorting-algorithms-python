"""
方法1
计数数组 = 最大值 + 1
"""
def counting_sort(arr, maxVal):
    n = len(arr)
    resArr = [0 for _ in range(n)]
    cntArr = [0 for _ in range(maxVal + 1)]

    for number in arr:
        cntArr[number] += 1
    
    i = 0
    for a in range(maxVal + 1):
        for _ in range(cntArr[a]):
            resArr[i] = a
            i += 1
    return resArr 


arr = [1, 14, 7, 1, 8, 2, 15, 4, 8, 10, 8, 3, 14, 5, 12, 4, 6, 10]
print("排序之前：", arr)
print("排序之后：", counting_sort(arr,max(arr)))

# 排序之前： [1, 14, 7, 1, 8, 2, 15, 4, 8, 10, 8, 3, 14, 5, 12, 4, 6, 10]
# 排序之后： [1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 8, 8, 10, 10, 12, 14, 14, 15]

"""
方法2
计数数组 = 最大值 - 最小值 + 1
"""

def counting_sort_2(arr, maxVal, minVal):
    n = len(arr)
    length = maxVal - minVal + 1
    # resArr = [0] * n
    # cntArr = [0] * length
    resArr = [0 for i in range(n)]
    cntArr = [0 for i in range(length)]
    for number in arr:
        cntArr[number - minVal] += 1   
    for i in range(1, length):
        cntArr[i] = cntArr[i] + cntArr[i - 1]    
    for j in range(n - 1, -1, -1):
        resArr[cntArr[arr[j] - minVal] - 1] = arr[j]
        cntArr[arr[j] - minVal] -= 1
    return resArr


arr = [1, 14, 7, 1, 8, 2, 15, 4, 8, 10, 8, 3, 14, 5, 12, 4, 6, 10]
print("排序之前：", arr)
print("排序之后: ", counting_sort_2(arr, max(arr), min(arr)))

# 排序之前： [1, 14, 7, 1, 8, 2, 15, 4, 8, 10, 8, 3, 14, 5, 12, 4, 6, 10]
# 排序之后： [1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 8, 8, 10, 10, 12, 14, 14, 15]