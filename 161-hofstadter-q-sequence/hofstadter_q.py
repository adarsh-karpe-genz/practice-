"""
Problem 161: Hofstadter Q-Sequence
Description:
Q(1) = 1, Q(2) = 1
Q(n) = Q(n - Q(n-1)) + Q(n - Q(n-2)) for n >= 3.
Displays chaotic behavior and sensitive dependence on initial values.
"""

def hofstadter_q_sequence(n: int) -> list[int]:
    """Generates the first n terms of Hofstadter Q-sequence."""
    if n <= 0:
        return []
    if n == 1:
        return [1]
    q = [0, 1, 1]
    for i in range(3, n + 1):
        next_val = q[i - q[i - 1]] + q[i - q[i - 2]]
        q.append(next_val)
    return q[1:]


def hofstadter_fluctuation_bounds(n: int) -> tuple[int, int]:
    """Computes (min, max) terms among the first n terms."""
    seq = hofstadter_q_sequence(n)
    return min(seq), max(seq)


if __name__ == "__main__":
    seq = hofstadter_q_sequence(15)
    expected = [1, 1, 2, 3, 3, 4, 5, 5, 6, 6, 6, 8, 8, 8, 10]
    assert seq == expected

    mn, mx = hofstadter_fluctuation_bounds(15)
    assert mn == 1 and mx == 10

    # Test monotonic average growth (overall Q(n) fluctuates around n / 2)
    seq_50 = hofstadter_q_sequence(50)
    assert abs(seq_50[-1] - 25) <= 10

    print("[PASS] Problem 161: Hofstadter Q-sequence and fluctuation bounds tests passed successfully.")
