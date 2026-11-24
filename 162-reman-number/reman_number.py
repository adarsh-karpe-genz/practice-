"""
Problem 162: Recamán's Sequence
Description:
a(0) = 0
a(n) = a(n-1) - n if a(n-1) - n > 0 and not already in sequence,
       else a(n-1) + n.
"""

def recaman_sequence(n: int) -> list[int]:
    """Generates the first n terms of Recamán's sequence."""
    if n <= 0:
        return []
    seq = [0]
    seen = {0}
    for i in range(1, n):
        back = seq[-1] - i
        if back > 0 and back not in seen:
            seq.append(back)
            seen.add(back)
        else:
            forward = seq[-1] + i
            seq.append(forward)
            seen.add(forward)
    return seq


def max_recaman(n: int) -> int:
    """Finds the maximum value achieved within the first n terms."""
    seq = recaman_sequence(n)
    return max(seq) if seq else 0


if __name__ == "__main__":
    seq = recaman_sequence(15)
    expected = [0, 1, 3, 6, 2, 7, 13, 20, 12, 21, 11, 22, 10, 23, 9]
    assert seq == expected
    assert max_recaman(15) == 23

    # Every element in sequence must be non-negative
    seq_50 = recaman_sequence(50)
    assert all(x >= 0 for x in seq_50)

    print("[PASS] Problem 162: Recamán's sequence and max value search tests passed successfully.")
