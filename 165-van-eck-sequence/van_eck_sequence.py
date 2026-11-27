"""
Problem 165: Van Eck's Sequence Generator
Defined by:
a_0 = 0
For n >= 0, if a_n has not appeared before, a_{n+1} = 0.
Else, a_{n+1} is how many steps back a_n last appeared.
"""

def van_eck_sequence(count: int) -> list[int]:
    """Generate the first count terms of Van Eck's sequence."""
    if count <= 0:
        return []
    seq = [0]
    last_pos = {}
    for i in range(count - 1):
        val = seq[-1]
        if val in last_pos:
            nxt = i - last_pos[val]
        else:
            nxt = 0
        last_pos[val] = i
        seq.append(nxt)
    return seq


def van_eck_first_occurrence(target: int, max_terms: int = 1000) -> int | None:
    """Finds the 0-based index of the first occurrence of target in Van Eck sequence."""
    seq = van_eck_sequence(max_terms)
    try:
        return seq.index(target)
    except ValueError:
        return None


def van_eck_max_value(count: int) -> int:
    """Returns the maximum value reached in the first count terms of Van Eck sequence."""
    seq = van_eck_sequence(count)
    return max(seq) if seq else 0


if __name__ == "__main__":
    expected = [0, 0, 1, 0, 2, 0, 2, 2, 1, 6]
    assert van_eck_sequence(10) == expected
    assert van_eck_sequence(1) == [0]
    assert van_eck_sequence(3) == [0, 0, 1]

    # Test first occurrence finder
    assert van_eck_first_occurrence(0) == 0
    assert van_eck_first_occurrence(1) == 2
    assert van_eck_first_occurrence(2) == 4
    assert van_eck_first_occurrence(6) == 9

    # Test peak value
    assert van_eck_max_value(10) == 6

    print("[PASS] Problem 165: van eck sequence passed all tests.")
