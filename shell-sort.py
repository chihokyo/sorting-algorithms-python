"""
# 这里的gap取什么是根据你的实际状况取最优，为了展示方便，选择了取半  
"""
def shell_sort(arr):  
    n = len(arr)  
    gap = n // 2  
    while gap > 0:  
        for i in range(gap,n):  
            j = i  
            while j > 0:  
                if arr[j] < arr[j-gap]:  
                    arr[j], arr[j-gap] = arr[j-gap], arr[j]  
                    j -= gap  
                else:  
                    break  
        gap //= 2   
    return arr  

arr = [66, 4, 8, 90, 13, 6, -9]  
print(shell_sort(arr))  