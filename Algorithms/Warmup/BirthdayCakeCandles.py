import sys

def birthdayCakeCandles(n, ar):
    tallest = 0
    number_tallest = 0
    for el in ar:
        if el > tallest:
            tallest = el
            number_tallest = 1
        elif el == tallest:
            number_tallest += 1
        else:
            pass
    return number_tallest

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)
