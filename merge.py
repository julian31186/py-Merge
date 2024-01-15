def merge(left,right):
    res = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        elif left[i] > right[j]:
            res.append(right[j])
            j += 1

    while i < len(left): 
        res.append(left[i])
        i += 1

    while j < len(right):
        res.append(right[j])
        j += 1
    
    return res

def mergesort(arr):
    l = 0
    r = len(arr) - 1
    mid = (l + r) // 2
    if l < r:
        left = mergesort(arr[l:mid + 1])
        right = mergesort(arr[mid + 1:r + 1])
        res = merge(left,right)
        return res
    return arr
