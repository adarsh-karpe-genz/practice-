"""
Problem 166: Kolakoski Sequence Generator
An infinite sequence of symbols {1, 2} that is its own run-length encoding.
Starts: 1, 2, 2, 1, 1, 2, 1, 2, 2, 1, 2, 2, 1, 1...
"""

def kolakoski_sequence(n: int) -> list[int]:
    """Generate first n terms of the {1, 2} Kolakoski sequence."""
    if n <= 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [1, 2]
    
    seq = [1, 2, 2]
    read_idx = 2
    curr_symbol = 1
    while len(seq) < n:
        count = seq[read_idx]
        seq.extend([curr_symbol] * count)
        curr_symbol = 2 if curr_symbol == 1 else 1
        read_idx += 1
    return seq[:n]

if __name__ == "__main__":
    expected = [1, 2, 2, 1, 1, 2, 1, 2, 2, 1]
    assert kolakoski_sequence(10) == expected
    assert kolakoski_sequence(3) == [1, 2, 2]
    assert kolakoski_sequence(1) == [1]
    print("[PASS] Problem 166: kolakoski sequence passed all tests.")
