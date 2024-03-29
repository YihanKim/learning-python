from math import sqrt, ceil

def get_primes(n):
    """Calculate a list of primes up to n (included). """

    primelist = []
    for candidate in range(2, n + 1):
        is_prime = True
        root = int(ceil(sqrt(candidate)))
        for prime in primelist:
            if prime > root:
                break
            if candidate % prime == 0:
                is_prime = False
                break
        if is_prime:
            primelist.append(candidate)
    return primelist

if __name__ == "__main__":
    print(get_primes(100))
