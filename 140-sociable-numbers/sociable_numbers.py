"""
Problem 140: Sociable Numbers Cycle Checker
Sociable numbers are numbers whose aliquot sums form a periodic sequence of period > 2.
(Period 1 = perfect, Period 2 = amicable).
"""

def aliquot_sum(n: int) -> int:
    """Sum of proper divisors of n."""
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

def find_aliquot_cycle(start: int, max_steps: int = 30) -> list[int] | None:
    """Return the cycle if start leads into a periodic aliquot cycle, else None."""
    path = []
    visited = {}
    curr = start
    for step in range(max_steps):
        if curr in visited:
            cycle_start = visited[curr]
            return path[cycle_start:]
        if curr == 0 or curr > 10_000_000:
            return None
        visited[curr] = step
        path.append(curr)
        curr = aliquot_sum(curr)
    return None

def is_sociable_cycle(cycle: list[int]) -> bool:
    """A sociable cycle must have length > 2."""
    return cycle is not None and len(cycle) > 2

if __name__ == "__main__":
    # Famous 5-cycle sociable numbers: 12496, 14288, 15472, 14536, 14264
    cycle_12496 = find_aliquot_cycle(12496)
    assert cycle_12496 == [12496, 14288, 15472, 14536, 14264]
    assert is_sociable_cycle(cycle_12496) is True
    # Amicable cycle has length 2, not sociable
    assert is_sociable_cycle([220, 284]) is False
    print("[PASS] Problem 140: sociable numbers passed all tests.")
