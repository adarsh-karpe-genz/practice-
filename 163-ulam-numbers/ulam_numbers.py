"""
Problem 163: Ulam Numbers
Description:
U(1) = 1, U(2) = 2.
Subsequent terms are the smallest integer greater than the previous term that
can be written uniquely as the sum of two distinct earlier terms.
"""

def ulam_sequence(n: int) -> list[int]:
    """Generates the first n Ulam numbers."""
    if n <= 0:
        return []
    if n == 1:
        return [1]
    ulam = [1, 2]
    candidate = 3
    while len(ulam) < n:
        count = 0
        left, right = 0, len(ulam) - 1
        while left < right:
            s = ulam[left] + ulam[right]
            if s == candidate:
                count += 1
                if count > 1:
                    break
                left += 1
                right -= 1
            elif s < candidate:
                left += 1
            else:
                right -= 1
        if count == 1:
            ulam.append(candidate)
        candidate += 1
    return ulam


def is_ulam_number(num: int, search_limit: int = 50) -> bool:
    """Checks if a given number num is within the first search_limit Ulam numbers."""
    seq = ulam_sequence(search_limit)
    return num in seq


if __name__ == "__main__":
    seq = ulam_sequence(15)
    expected = [1, 2, 3, 4, 6, 8, 11, 13, 16, 18, 26, 28, 36, 38, 47]
    assert seq == expected

    assert is_ulam_number(26) is True
    assert is_ulam_number(5) is False
    assert is_ulam_number(7) is False

    print("[PASS] Problem 163: Ulam numbers sequence and membership checker tests passed successfully.")
