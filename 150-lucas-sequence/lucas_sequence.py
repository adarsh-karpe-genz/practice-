"""
Problem 150: Lucas Sequence
Description:
Generates the Lucas sequence numbers.
L(0) = 2, L(1) = 1, L(n) = L(n-1) + L(n-2) for n >= 2.
"""

def lucas_sequence(n: int) -> list[int]:
    """Generates the first n numbers of the Lucas sequence."""
    if n <= 0:
        return []
    if n == 1:
        return [2]
    seq = [2, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq


def lucas_number_binet(n: int) -> int:
    """
    Computes the n-th Lucas number using Binet-like closed form:
    L(n) = phi^n + psi^n where phi = (1 + sqrt(5))/2 and psi = (1 - sqrt(5))/2.
    """
    phi = (1 + 5 ** 0.5) / 2
    psi = (1 - 5 ** 0.5) / 2
    return round(phi ** n + psi ** n)


if __name__ == "__main__":
    seq = lucas_sequence(10)
    expected = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76]
    assert seq == expected

    for i in range(10):
        assert lucas_number_binet(i) == expected[i], f"Binet formula mismatch at index {i}"

    print("[PASS] Problem 150: Lucas Sequence tests passed successfully.")
