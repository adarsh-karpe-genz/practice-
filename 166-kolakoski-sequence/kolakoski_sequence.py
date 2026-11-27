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


def kolakoski_density(n: int) -> float:
    """
    Computes density of symbol 1 in first n terms of Kolakoski sequence.
    Conjectured to converge asymptotically to 0.5.
    """
    if n <= 0:
        return 0.0
    seq = kolakoski_sequence(n)
    return seq.count(1) / n


def verify_kolakoski_run_length(seq: list[int]) -> bool:
    """
    Verifies that the run lengths of the generated sequence match the sequence itself.
    """
    if len(seq) < 3:
        return True
    run_lengths = []
    i = 0
    while i < len(seq):
        run = 1
        while i + 1 < len(seq) and seq[i] == seq[i + 1]:
            i += 1
            run += 1
        run_lengths.append(run)
        i += 1
    # The run lengths prefix must match seq
    prefix_len = min(len(run_lengths), len(seq))
    return run_lengths[:prefix_len] == seq[:prefix_len]


if __name__ == "__main__":
    expected = [1, 2, 2, 1, 1, 2, 1, 2, 2, 1]
    assert kolakoski_sequence(10) == expected
    assert kolakoski_sequence(3) == [1, 2, 2]
    assert kolakoski_sequence(1) == [1]

    # Verify self-generating run-length property
    seq_50 = kolakoski_sequence(50)
    assert verify_kolakoski_run_length(seq_50) is True

    # Density of 1s in first 100 terms is close to 0.5
    density_100 = kolakoski_density(100)
    assert abs(density_100 - 0.5) < 0.1

    print("[PASS] Problem 166: kolakoski sequence passed all tests.")
