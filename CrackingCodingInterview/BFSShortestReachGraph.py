class Graph:
    def __init__(self, data):



t = input()
for i in range(t):
    n, m = [int(x) for x in raw_input().split()]
    graph = Graph(n)
    for i in xrange(m):
        x, y = [int(x) for x in raw_input().split()]
        graph.connect(x - 1, y - 1)
    s = input()
    graph.find_all_distances(s - 1)
