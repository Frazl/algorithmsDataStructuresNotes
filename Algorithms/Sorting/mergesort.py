def merge(left, right):
    result = []
    i = j = 0 
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1 
        else:
            result.append(right[j])
            j += 1 
        
    result += left[i:]
    result += right[j:]
        
    return result

def merge_sort(a):

    if len(a) <= 1:
        return a 
    
    middle = len(a) // 2 
    left = a[:middle]
    right = a[middle:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)



a = [12,41,5,126,12,124,12,1,5,124,12,61,51,25,21,167,16,34,754,7845,724,412,5,2346,3245,236,326,23,6723,52,7634,5324,634,63,46,346,34,6213,623,67234,53,2]
print(merge_sort(a))