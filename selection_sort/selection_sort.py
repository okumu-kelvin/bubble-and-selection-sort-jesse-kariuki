def selection_sort(arr):
    # TODO: Implement selection sort

    n= len(arr)

    for i in range(n):
        min = i
        for j in range(i+1,n):
            if arr[j] < arr[min]:
                min = j

            (arr[i],arr[min]) = (arr[min],arr[i])

    return arr

print(selection_sort([3,2,1,5,6,7,8,9,10]))