"""
Problem 149: Chinese Remainder Theorem Solver
Given system of congruences:
x = a_1 (mod m_1)
x = a_2 (mod m_2)
...
where m_i are pairwise coprime, find smallest non-negative integer solution x.
"""
import math
from functools import reduce

def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    return gcd, y1 - (b // a) * x1, x1

def mod_inv(a: int, m: int) -> int:
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("Moduli must be coprime")
    return (x % m + m) % m

def solve_crt(remainders: list[int], moduli: list[int]) -> int:
    """Solve system x = remainders[i] mod moduli[i]."""
    total_m = reduce(lambda x, y: x * y, moduli, 1)
    x = 0
    for r_i, m_i in zip(remainders, moduli):
        m_partial = total_m // m_i
        inv = mod_inv(m_partial, m_i)
        x += r_i * m_partial * inv
    return x % total_m

if __name__ == "__main__":
    # x = 2 mod 3, x = 3 mod 5, x = 2 mod 7 -> solution is 23
    r = [2, 3, 2]
    m = [3, 5, 7]
    sol = solve_crt(r, m)
    assert sol == 23
    for rem, mod in zip(r, m):
        assert sol % mod == rem

    # x = 1 mod 2, x = 2 mod 3, x = 3 mod 5 -> solution is 23
    assert solve_crt([1, 2, 3], [2, 3, 5]) == 23
    print("[PASS] Problem 149: chinese remainder theorem passed all tests.")
