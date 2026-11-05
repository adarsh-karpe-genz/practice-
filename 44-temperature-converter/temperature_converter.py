"""
Problem 44: Temperature Converter (Celsius, Fahrenheit, Kelvin)
Difficulty: Beginner / Easy

Problem Statement:
Convert temperatures between Celsius (C), Fahrenheit (F), and Kelvin (K).
Formulas:
- C to F: (C * 9/5) + 32
- F to C: (F - 32) * 5/9
- C to K: C + 273.15
- K to C: K - 273.15

Concepts:
- Floating point arithmetic and rounding
- Function modularity
- Dictionary dispatch or conditional conversion
"""

def celsius_to_fahrenheit(c: float) -> float:
    return round((c * 9 / 5) + 32, 2)


def fahrenheit_to_celsius(f: float) -> float:
    return round((f - 32) * 5 / 9, 2)


def celsius_to_kelvin(c: float) -> float:
    return round(c + 273.15, 2)


def kelvin_to_celsius(k: float) -> float:
    return round(k - 273.15, 2)


def convert_temperature(val: float, from_unit: str, to_unit: str) -> float:
    """Convert temperature across C, F, K units."""
    u1, u2 = from_unit.upper(), to_unit.upper()
    if u1 == u2:
        return round(val, 2)
    # Convert to Celsius first
    c = val if u1 == "C" else (val - 32) * 5 / 9 if u1 == "F" else val - 273.15
    # Convert from Celsius to target
    res = c if u2 == "C" else c * 9 / 5 + 32 if u2 == "F" else c + 273.15
    return round(res, 2)


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 44: Temperature Converter Tests")
    print("=" * 50)

    assert celsius_to_fahrenheit(0) == 32.0
    assert celsius_to_fahrenheit(100) == 212.0
    assert fahrenheit_to_celsius(32) == 0.0
    assert fahrenheit_to_celsius(212) == 100.0
    assert celsius_to_kelvin(0) == 273.15
    assert kelvin_to_celsius(273.15) == 0.0

    print("0 C -> 32.0 F")
    print("100 C -> 212.0 F")
    print("32 F -> 0.0 C")
    print("0 C -> 273.15 K")

    assert convert_temperature(100, "C", "F") == 212.0
    assert convert_temperature(32, "F", "C") == 0.0
    assert convert_temperature(0, "C", "K") == 273.15
    print("\n[PASS] All Temperature Converter tests passed successfully!")
