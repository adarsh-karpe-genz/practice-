"""
Problem 157: Stern-Brocot (Stern's Diatomic) Sequence
Defined by:
s_0 = 0, s_1 = 1
s_{2n} = s_n
s_{2n+1} = s_n + s_{n+1}
Every positive rational number p/q appears as s_n / s_{n+1} in lowest terms.
"""

def stern_sequence(n_terms: int) -> list[int]:
    """Generate the first n_terms of the Stern-Brocot sequence."""
    if n_terms <= 0:
        return []
    if n_terms == 1:
        return [0]
    
    seq = [0, 1]
    while len(seq) < n_terms:
        n = len(seq)
        if n % 2 == 0:
            seq.append(seq[n // 2])
        else:
            half = n // 2
            seq.append(seq[half] + seq[half + 1])
    return seq[:n_terms]

if __name__ == "__main__":
    expected = [0, 1, 1, 2, 1, 3, 2, 3, 1, 4]
    res = stern_sequence(10)
    assert res == expected
    assert stern_sequence(1) == [0]
    assert stern_sequence(2) == [0, 1]
    print("[PASS] Problem 157: stern brocot sequence passed all tests.")
