
import sys
import heapq
import bisect
import timeit

n = int(raw_input().strip())
h_min = []  # should be all large numbers
h_max = []  # should be all small numbers
a_i = 0
# start_time = timeit.default_timer()
for a_i in xrange(n):
    a_t = int(raw_input().strip())
    # if len(h_min) > 0 and a_t >= h_min[0]:
    #     heapq.heappush(h_min, a_t)
    # else:
    #     heapq.heappush(h_max, -1.0*a_t)
    # if len(h_min) > len(h_max) + 1:
    #     heapq.heappush(h_max, heapq.heappop(h_min) * -1.0)
    # if len(h_max) > len(h_min) + 1:
    #     heapq.heappush(h_min, heapq.heappop(h_max) * -1.0)
    #
    # # printing
    # if len(h_max) > len(h_min):
    #     print float(-1 *h_max[0])
    # elif len(h_min) > len(h_max):
    #     print float(h_min[0])
    # else:
    #     print (h_min[0] + -1 * h_max[0]) / 2.0



    # # add to the min heap if there are no elements in either heap
    if len(h_min) == 0 and len(h_max) == 0:
        heapq.heappush(h_min, a_t)
    # if there is already an element in the heaps, then compare the new element with the ones in the heap
    else:
        # put in the list with fewer elements
        if len(h_max) > len(h_min):
            heapq.heappush(h_min, a_t)
        else:
            heapq.heappush(h_max, a_t*-1)
        # switch if elements chosen are in wrong list
        if h_max[0] * -1 > h_min[0]:
            heapq.heappush(h_max, -1* heapq.heappop(h_min))
            heapq.heappush(h_min, heapq.heappop(h_max) * -1)

    # printing
    if len(h_max) > len(h_min):
        print float(-1 * h_max[0])
    elif len(h_min) > len(h_max):
        print float(h_min[0])
    else:
        print (h_min[0] + -1 * h_max[0]) / 2.0

    # bisect.insort(h_min, a_t)
    # list_size = len(h_min)
    # if list_size % 2 == 0:
    #     print (h_min[list_size/2-1] + h_min[list_size/2])/2.0
    # else:
    #     print float(h_min[(list_size+1)/2-1])


# print 'Took %d seconds' %(timeit.default_timer() - start_time)