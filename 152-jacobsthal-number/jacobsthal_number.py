"""
Problem 152: Jacobsthal and Jacobsthal-Lucas Sequences
Description:
Jacobsthal numbers: J(0) = 0, J(1) = 1, J(n) = J(n-1) + 2 * J(n-2).
Companion Jacobsthal-Lucas numbers: j(0) = 2, j(1) = 1, j(n) = j(n-1) + 2 * j(n-2).
"""

def jacobsthal_sequence(n: int) -> list[int]:
    """Generates the first n Jacobsthal numbers."""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    seq = [0, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + 2 * seq[-2])
    return seq


def jacobsthal_lucas_sequence(n: int) -> list[int]:
    """Generates the first n Jacobsthal-Lucas numbers."""
    if n <= 0:
        return []
    if n == 1:
        return [2]
    seq = [2, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + 2 * seq[-2])
    return seq


def jacobsthal_closed_form(n: int) -> int:
    """Computes J(n) using closed form: J(n) = (2^n - (-1)^n) // 3."""
    return (2**n - (-1)**n) // 3


if __name__ == "__main__":
    j_seq = jacobsthal_sequence(10)
    expected_j = [0, 1, 1, 3, 5, 11, 21, 43, 85, 171]
    assert j_seq == expected_j

    for i in range(10):
        assert jacobsthal_closed_form(i) == expected_j[i]

    jl_seq = jacobsthal_lucas_sequence(8)
    expected_jl = [2, 1, 5, 7, 17, 31, 65, 127]
    assert jl_seq == expected_jl

    print("[PASS] Problem 152: Jacobsthal and Jacobsthal-Lucas tests passed successfully.")
