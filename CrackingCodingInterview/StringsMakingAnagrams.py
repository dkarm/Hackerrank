def number_needed(a, b):
    array_a = [0]*26
    array_b = [0]*26
    for e in a:
        array_a[ord(e) - ord('a')] += 1
    for e in b:
        array_b[ord(e) - ord('a')] += 1
    difference = [abs(x1 - x2) for (x1, x2) in zip(array_a, array_b)]
    return sum(difference)


a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)

