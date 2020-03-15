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

arr = [ 5, 6, 18, 4, 9, -5, 3, 11]     
print(while_insertion_sort(arr))


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

arr = [ 5, 6, 18, 4, 9, -5, 3, 11]
print(for_insertion_sort(arr))     