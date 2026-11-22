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

def classify_aliquot_sequence(n: int) -> str:
    """Classify aliquot path: 'terminating' (ends at 0), 'perfect', 'amicable', or 'cyclic'."""
    seq = generate_aliquot_sequence(n, max_steps=30)
    if seq[-1] == 0:
        return "terminating"
    if len(seq) >= 2 and seq[-1] == seq[-2]:
        return "perfect"
    if len(seq) >= 3 and seq[-1] == seq[-3]:
        return "amicable"
    return "cyclic"


if __name__ == "__main__":
    # For a prime like 11: 11 -> 1 -> 0
    assert generate_aliquot_sequence(11) == [11, 1, 0]
    # For perfect number 6: 6 -> 6 (cycle)
    assert generate_aliquot_sequence(6) == [6, 6]
    # For amicable pair 220: 220 -> 284 -> 220
    assert generate_aliquot_sequence(220) == [220, 284, 220]
    assert classify_aliquot_sequence(11) == "terminating"
    assert classify_aliquot_sequence(6) == "perfect"
    assert classify_aliquot_sequence(220) == "amicable"
    print("[PASS] Problem 139: aliquot sequence passed all tests.")
