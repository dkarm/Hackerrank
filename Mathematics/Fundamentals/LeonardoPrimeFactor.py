
def sievePrimes(n, primes):
    primes[0] = 1
    primes[1] = 1
    i = 2
    while i < n:
        j = 2
        if primes[i] == 0:
            while i * j < n:
                primes[i * j] = 1
                j += 1
        i += 1

def find_next_prime(primes):
    last = primes[-1] + 1
    while True:
        found_prime = 0
        for idx, prime in enumerate(primes):
            if last % prime ==0:
                break
            if idx == len(primes) -1 and last%prime !=0:
                return last
        last +=1

def find_primes_lower(number):
    current = 1
    count = 0
    while current <= number:







n = int(raw_input())
primes = 100000000000000000*[0]
sievePrimes(len(primes), primes)

for i in range(n):
    a = int(raw_input())
    print find_prime_factors(a)
