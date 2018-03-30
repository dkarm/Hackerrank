

import sys

def plusMinus(arr):
    pos = len([x for x in arr if x > 0])
    neg = len([x for x in arr if x < 0])
    zero = len([x for x in arr if x == 0])
    print float(pos)/len(arr)
    print float(neg) / len(arr)
    print float(zero) / len(arr)

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    plusMinus(arr)
