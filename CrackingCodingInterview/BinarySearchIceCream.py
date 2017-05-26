def binary_search(search_array, target, index_array):
    n = len(search_array)
    bottom = 0
    middle = n/2
    top = n - 1
    if n==1 and search_array[0]==target:
        return index_array[0]
    elif search_array[middle] == target:
        return index_array[middle]
    elif search_array[bottom]==target:
        return index_array[bottom]
    elif search_array[top] == target:
        return index_array[top]
    elif search_array[bottom] < target < search_array[middle]:
        return binary_search(search_array[bottom:middle], target, index_array[bottom:middle])
    elif search_array[middle] < target < search_array[top]:
        return binary_search(search_array[middle:top], target, index_array[middle:top])
    else:
        return None


t = int(raw_input().strip())
for a0 in xrange(t):
    m = int(raw_input().strip())
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    index_array = [0]*n
    # print index_array
    index_array = [idx +1 for idx, point in enumerate(index_array)]

    to_sort = zip(a, index_array)
    to_sort.sort(key = lambda t: t[0])
    a, index_array = zip(*to_sort)
    a = [x for x in a if x < m]
    for idx, el in enumerate(a[:-1]):
        target = m-el
        x = binary_search(a[idx+1:],target, index_array[idx+1:])
        if x is not None:
            first = index_array[idx]
            second = x
            if first > second:
                print second, first
            else:
                print first, second
            break