"""
Problem 163: Ulam Numbers Generator
Ulam sequence starts with U_1 = 1, U_2 = 2.
Each subsequent term is the smallest integer > previous that can be written as
the sum of two distinct earlier terms in UNIQUE way.
"""

def ulam_sequence(count: int) -> list[int]:
    """Generate the first count Ulam numbers."""
    if count <= 0:
        return []
    if count == 1:
        return [1]
    if count == 2:
        return [1, 2]
    
    ulam = [1, 2]
    ulam_set = {1, 2}
    candidate = 3
    while len(ulam) < count:
        ways = 0
        for i in range(len(ulam)):
            a = ulam[i]
            b = candidate - a
            if b > a and b in ulam_set:
                ways += 1
                if ways > 1:
                    break
        if ways == 1:
            ulam.append(candidate)
            ulam_set.add(candidate)
        candidate += 1
    return ulam

if __name__ == "__main__":
    expected = [1, 2, 3, 4, 6, 8, 11, 13, 16]
    assert ulam_sequence(9) == expected
    assert ulam_sequence(2) == [1, 2]
    print("[PASS] Problem 163: ulam numbers passed all tests.")
