"""
Problem 162: Recamán's Sequence Generator
Defined by:
a_0 = 0
a_n = a_{n-1} - n if (a_{n-1} - n > 0 and not already in sequence) else a_{n-1} + n.
"""

def recaman_sequence(count: int) -> list[int]:
    """Generate the first count terms of Recaman's sequence."""
    if count <= 0:
        return []
    seq = [0]
    seen = {0}
    for n in range(1, count):
        prev = seq[-1]
        step_down = prev - n
        if step_down > 0 and step_down not in seen:
            seq.append(step_down)
            seen.add(step_down)
        else:
            step_up = prev + n
            seq.append(step_up)
            seen.add(step_up)
    return seq

if __name__ == "__main__":
    expected = [0, 1, 3, 6, 2, 7, 13, 20, 12, 21]
    assert recaman_sequence(10) == expected
    assert recaman_sequence(1) == [0]
    assert recaman_sequence(4) == [0, 1, 3, 6]
    print("[PASS] Problem 162: recaman sequence passed all tests.")
