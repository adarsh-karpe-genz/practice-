"""
Problem 139: Aliquot Sequence Generator
An aliquot sequence starts with a positive integer k, and each subsequent term
is the sum of proper divisors of the previous term.
"""

def proper_divisors_sum(n: int) -> int:
    """Return sum of proper divisors of n."""
    if n <= 1:
        return 0
    total = 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            total += d
            if d * d != n:
                total += n // d
        d += 1
    return total

def generate_aliquot_sequence(n: int, max_steps: int = 20) -> list[int]:
    """Generate the aliquot sequence starting at n until 0, cycle, or max_steps."""
    seq = [n]
    seen = {n}
    curr = n
    for _ in range(max_steps):
        nxt = proper_divisors_sum(curr)
        seq.append(nxt)
        if nxt == 0 or nxt in seen:
            break
        seen.add(nxt)
        curr = nxt
    return seq

if __name__ == "__main__":
    # For a prime like 11: 11 -> 1 -> 0
    assert generate_aliquot_sequence(11) == [11, 1, 0]
    # For perfect number 6: 6 -> 6 (cycle)
    assert generate_aliquot_sequence(6) == [6, 6]
    # For amicable pair 220: 220 -> 284 -> 220
    assert generate_aliquot_sequence(220) == [220, 284, 220]
    print("[PASS] Problem 139: aliquot sequence passed all tests.")
