"""
Problem 151: Pell Sequence & Pell-Lucas Numbers
Description:
The Pell sequence is defined by recurrence:
P(0) = 0, P(1) = 1, P(n) = 2 * P(n-1) + P(n-2) for n >= 2.
Companion Pell-Lucas sequence:
Q(0) = 2, Q(1) = 2, Q(n) = 2 * Q(n-1) + Q(n-2) for n >= 2.
"""

def pell_sequence(n: int) -> list[int]:
    """Generates the first n terms of the Pell sequence."""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    seq = [0, 1]
    for _ in range(2, n):
        seq.append(2 * seq[-1] + seq[-2])
    return seq


def pell_lucas_sequence(n: int) -> list[int]:
    """Generates the first n terms of the companion Pell-Lucas sequence Q(n)."""
    if n <= 0:
        return []
    if n == 1:
        return [2]
    seq = [2, 2]
    for _ in range(2, n):
        seq.append(2 * seq[-1] + seq[-2])
    return seq


if __name__ == "__main__":
    pell = pell_sequence(10)
    expected_pell = [0, 1, 2, 5, 12, 29, 70, 169, 408, 985]
    assert pell == expected_pell

    pell_lucas = pell_lucas_sequence(8)
    expected_lucas = [2, 2, 6, 14, 34, 82, 198, 478]
    assert pell_lucas == expected_lucas

    # Relation check: Q(n) = 2 * P(n+1) - 2 * P(n) for n >= 0
    # or Q(n)^2 - 8 * P(n)^2 = 4 * (-1)^n
    for n in range(len(pell_lucas)):
        assert pell_lucas[n]**2 - 8 * pell[n]**2 == 4 * ((-1)**n)

    print("[PASS] Problem 151: Pell Sequence and Pell-Lucas companion tests passed successfully.")
