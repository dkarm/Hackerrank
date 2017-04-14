def array_left_rotation(a, n, k):
    new_array = [0]*len(a)
    for e in range(0, len(a)):
        new_position = (e-k) % len(a)
        new_array[new_position] = a[e]
    return new_array



n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str, answer))