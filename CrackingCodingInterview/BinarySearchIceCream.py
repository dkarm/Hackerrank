def create_total_cost(list_one):
    total_cost = []
    ice_cream1 = []
    ice_cream2 = []
    for idx, e in enumerate(list_one):
        for idxf, f in enumerate(list_one):
            if e != f:
                total_cost.append(e + f)
                ice_cream1.append(idx)
                ice_cream2.append(idxf)
    return zip(total_cost, ice_cream1, ice_cream2)


t = int(raw_input().strip())


def binary_search(list_two_matrix, target):
    n = len(list_two)
    bottom = 0
    middle = n/2
    top = n

    list_two = list_two_matrix[:, 0]

    if n ==1:
        return list_two
    if list_two[middle] > target and list_two[bottom] < target:
        binary_search(list_two_matrix[bottom:middle, :])
    elif list_two[middle] < target and list_two[top] > target:
        binary_search(list_two_matrix[middle:top, :])

for a0 in xrange(t):
    m = int(raw_input().strip())
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    total_cost_matrix = create_total_cost(a)
    total_cost_matrix.sort(key=lambda t: t[0])


