"""
Problem 149: Chinese Remainder Theorem (CRT)
Description:
Solves a system of simultaneous congruences:
    x ≡ rem[0] (mod num[0])
    x ≡ rem[1] (mod num[1])
    ...
    x ≡ rem[k-1] (mod num[k-1])
assuming all moduli in num are pairwise coprime.
"""

from math import gcd

def are_pairwise_coprime(moduli: list[int]) -> bool:
    """Checks if all integers in moduli list are pairwise coprime."""
    n = len(moduli)
    for i in range(n):
        for j in range(i + 1, n):
            if gcd(moduli[i], moduli[j]) != 1:
                return False
    return True


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = extended_gcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)


def mod_inverse(a: int, m: int) -> int:
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError(f"Modular inverse does not exist for a={a}, m={m}")
    return (x % m + m) % m


def chinese_remainder_theorem(num: list[int], rem: list[int]) -> int:
    """
    Finds the smallest positive integer x satisfying the system of congruences.
    """
    if len(num) != len(rem):
        raise ValueError("Lengths of num and rem lists must match.")
    if not are_pairwise_coprime(num):
        raise ValueError("Moduli must be pairwise coprime.")

    prod = 1
    for n in num:
        prod *= n

    result = 0
    for n_i, r_i in zip(num, rem):
        pp = prod // n_i
        inv = mod_inverse(pp, n_i)
        result += r_i * pp * inv

    return result % prod


if __name__ == "__main__":
    assert are_pairwise_coprime([3, 5, 7]) is True
    assert are_pairwise_coprime([3, 6, 7]) is False

    num = [3, 5, 7]
    rem = [2, 3, 2]
    ans = chinese_remainder_theorem(num, rem)
    assert ans == 23
    for n_i, r_i in zip(num, rem):
        assert ans % n_i == r_i

    print("[PASS] Problem 149: Chinese Remainder Theorem tests passed successfully.")
