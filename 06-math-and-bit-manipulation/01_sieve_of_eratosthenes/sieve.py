"""
Problem: Sieve of Eratosthenes

Time Complexity: O(N log log N)
Space Complexity: O(N)
"""

from typing import List

def sieve(n: int) -> List[int]:
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False

    return [i for i in range(2, n + 1) if is_prime[i]]

if __name__ == "__main__":
    print("[Python] Sieve of Eratosthenes Test")
    primes_30 = sieve(30)
    print("Primes up to 30:", primes_30)
    assert primes_30 == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    print("Sieve test passed!")
