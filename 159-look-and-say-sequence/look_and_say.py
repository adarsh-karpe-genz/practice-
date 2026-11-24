"""
Problem 159: Look-and-Say Sequence
Description:
Generates the Look-and-Say sequence starting from '1'.
1, 11, 21, 1211, 111221, 312211, ...
"""

def next_look_and_say(s: str) -> str:
    """Computes the next term in the Look-and-Say sequence."""
    result = []
    i = 0
    n = len(s)
    while i < n:
        count = 1
        while i + 1 < n and s[i] == s[i + 1]:
            i += 1
            count += 1
        result.append(f"{count}{s[i]}")
        i += 1
    return "".join(result)


def look_and_say_sequence(n: int, seed: str = "1") -> list[str]:
    """Generates the first n terms of the Look-and-Say sequence."""
    if n <= 0:
        return []
    seq = [seed]
    for _ in range(1, n):
        seq.append(next_look_and_say(seq[-1]))
    return seq


def length_growth_ratio(n: int) -> float:
    """
    Computes ratio len(term[n]) / len(term[n-1]), which asymptotically
    approaches Conway's constant lambda ≈ 1.303577269...
    """
    seq = look_and_say_sequence(n)
    if len(seq) < 2:
        return 0.0
    return len(seq[-1]) / len(seq[-2])


if __name__ == "__main__":
    seq = look_and_say_sequence(6)
    expected = ["1", "11", "21", "1211", "111221", "312211"]
    assert seq == expected

    # Ratio approaches Conway's constant for larger n
    seq_15 = look_and_say_sequence(15)
    ratios = [len(seq_15[i]) / len(seq_15[i - 1]) for i in range(10, 15)]
    avg_ratio = sum(ratios) / len(ratios)
    assert abs(avg_ratio - 1.303) < 0.1

    print("[PASS] Problem 159: Look-and-Say sequence and Conway growth ratio tests passed successfully.")
