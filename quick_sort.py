def quick_sort(list_of_ints, start, end):
    if start >= end:
        return
    right_eq = start
    low = start - 1
    high = end + 1
    pivot = list_of_ints[start]
    i = start + 1
    while i < high:
        if i > end:
            break
        if list_of_ints[i] == pivot:
            right_eq += 1
            i += 1
            continue
        if list_of_ints[i] > pivot:
            high -= 1
            list_of_ints[i], list_of_ints[high] = list_of_ints[high], list_of_ints[i]
            continue
        if list_of_ints[i] < pivot:
            low += 1
            right_eq += 1
            list_of_ints[low], list_of_ints[i] = list_of_ints[i], list_of_ints[low]
            i += 1
            continue
    quick_sort(list_of_ints, start, low)
    quick_sort(list_of_ints, high, end)


list_of_ints = list(map(int, input().split(" ")))
quick_sort(list_of_ints, 0, len(list_of_ints)-1)
print(' '.join(str(i) for i in list_of_ints))
