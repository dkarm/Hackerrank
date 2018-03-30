import sys

def nonDivisibleSubset(k, arr):
    max_length = 0


if __name__ == "__main__":
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = map(int, raw_input().strip().split(' '))
    result = nonDivisibleSubset(k, arr)
    print result