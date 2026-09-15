"""
Problem 50: Decimal to Binary and Binary to Decimal Converter
Difficulty: Beginner / Easy

Problem Statement:
Convert a non-negative integer from Decimal to Binary representation (as a string)
and from Binary (string) back to Decimal integer.
Example:
  Decimal 10 -> Binary "1010"
  Binary "1010" -> Decimal 10

Concepts:
- Repeated division by 2 and remainder collection
- Powers of 2 positional summation
- Built-in bin() and int(s, 2) comparisons
"""

def decimal_to_binary(n: int) -> str:
    """Convert decimal integer to binary string."""
    if n == 0:
        return "0"
    bits = []
    while n > 0:
        bits.append(str(n % 2))
        n //= 2
    return "".join(reversed(bits))


def binary_to_decimal(b_str: str) -> int:
    """Convert binary string to decimal integer."""
    decimal_val = 0
    for bit in b_str:
        decimal_val = decimal_val * 2 + int(bit)
    return decimal_val


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 50: Binary Decimal Converter Tests")
    print("=" * 50)

    test_cases = [0, 1, 2, 5, 10, 16, 42, 255]

    for num in test_cases:
        b = decimal_to_binary(num)
        d = binary_to_decimal(b)
        print(f"Dec: {num:3d} <-> Bin: {b:>8} | Roundtrip Dec: {d:3d}")
        assert b == bin(num)[2:], f"Binary conversion failed for {num}"
        assert d == num, f"Decimal roundtrip failed for {num}"

    print("\n[PASS] All Binary Decimal Converter tests passed successfully!")
