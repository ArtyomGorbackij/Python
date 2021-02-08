def bin_search(array, element, start, end):
    if element in array:
        mid = (start + end) // 2
        if end < start or start > end:
            return -1
        if element < array[mid]:
            return bin_search(array, element, start, mid-1)
        elif element > array[mid]:
            return bin_search(array, element, mid+1, end)
        if element == array[mid]:
            try:
                assert bin_search(array, element, start, mid-1) != -1
                return bin_search(array, element, start, mid-1)
            except AssertionError:
                return mid
    else:
        return -1


try:
    int_array = list(map(int, input().split(" ")))
except ValueError:
    int_array = []

while True:
    try:
        for line in iter(input, '') :
            srch = line
            element = int(srch.lstrip("search "))
            print(bin_search(int_array, element, 0, len(int_array)))
    except EOFError:
        break