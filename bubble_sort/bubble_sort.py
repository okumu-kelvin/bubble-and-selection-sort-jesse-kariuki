def bubble_sort(unsorted_list):
    # TODO: Implement bubble sort
    for i in range(len(unsorted_list)):
        for j in range(len(unsorted_list)-i-1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                temp = unsorted_list[j]
                unsorted_list[j] = unsorted_list[j + 1]
                unsorted_list[j + 1] = temp

    return unsorted_list

print(bubble_sort([15, 6, 17, 8, 19, 10,1]))
