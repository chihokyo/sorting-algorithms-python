"""
while循环做法
"""

def while_insertion_sort(arr: list)-> list:
    n = len(arr)
    for i in range(1,n):
        j = i
        while j > 0:
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j-=1
            else:
                break
    return arr

arr = [ 12, 34, 54, 2, 3, -1, 0, -16]     
print(while_insertion_sort(arr))

# result
# [-16, -1, 0, 2, 3, 12, 34, 54]


"""
for循环做法
"""
def for_insertion_sort(arr: list)-> list:
    n = len(arr)
    for i in range(1,n):
        for j in range(i,0,-1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

arr = [ 12, 34, 54, 2, 3, -1, 0, -16] 
print(for_insertion_sort(arr))

# result
# [-16, -1, 0, 2, 3, 12, 34, 54]