n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))

num_total_swaps = 0


while True:
    i = 0
    swaps_in_iter = 0
    while (i < n-1):
        if a[i] > a[i+1]:
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp
            swaps_in_iter += 1
        i += 1
    num_total_swaps = num_total_swaps + swaps_in_iter
    if swaps_in_iter ==0:
        break

print "Array is sorted in %d swaps." % num_total_swaps
print "First Element:", a[0]
print "Last Element:", a[n-1]
