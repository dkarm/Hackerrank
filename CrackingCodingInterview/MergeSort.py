import timeit


def count_inversions(array, inversions):
    if len(array) > 1:
        left, inversions_right = count_inversions(array[0:len(array) / 2], inversions)
        right, inversions_left = count_inversions(array[len(array) / 2:], inversions)
        inversions = inversions_right + inversions_left
        return merge(left, right, inversions)
    else:
        return array, inversions

def merge(array_left, array_right, inversions):
    new_array = [0] * (len(array_left) + len(array_right))
    new_array_counter = 0
    right_counter = 0
    for i in range(len(array_left)):
        if right_counter == len(array_right):
            new_array[new_array_counter: new_array_counter + len(array_left[i:])] = array_left[i:]
            new_array_counter += len(array_left[i:])
            break
        elif array_left[i] <= array_right[right_counter]:
            new_array[new_array_counter] = array_left[i]
            new_array_counter += 1
        else:
            while right_counter < len(array_right) and array_right[right_counter] < array_left[i]:
                new_array[new_array_counter] = array_right[right_counter]
                new_array_counter += 1
                right_counter += 1
                inversions += len(array_left) - i
            new_array[new_array_counter] = array_left[i]
            new_array_counter +=1
    new_array[new_array_counter:] = array_right[right_counter:]

    return new_array, inversions


t = int(raw_input().strip())

start_time = timeit.default_timer()
for a0 in xrange(t):
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    print count_inversions(arr, 0)[1]


print 'it took', (timeit.default_timer() - start_time)
