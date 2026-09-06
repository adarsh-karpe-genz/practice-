"""
Problem 26: Check Balanced Parentheses Using Stack
Difficulty: Beginner / Easy

Problem Statement:
Given a string containing only '(', ')', '{', '}', '[' and ']',
determine if the input string has all brackets balanced and properly nested.
Examples:
  "([]){}" -> True
  "([)]"   -> False
  "{[]}"   -> True
  ""       -> True (empty string is valid)

Concepts:
- Stack data structure (LIFO: Last In, First Out)
- List as stack using .append() and .pop()
- Mapping of closing-to-opening brackets with dict
"""

def is_balanced(s: str) -> bool:
    """Check if brackets in string are balanced using a stack."""
    stack = []
    closing_to_opening = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in closing_to_opening:
            if not stack or stack[-1] != closing_to_opening[char]:
                return False
            stack.pop()

    return len(stack) == 0


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 26: Balanced Parentheses Tests")
    print("=" * 50)

    test_cases = [
        ("([]){}", True),
        ("{[]}", True),
        ("((()))", True),
        ("", True),
        ("([)]", False),
        ("(((", False),
        ("])}", False),
        ("{[()]}", True),
    ]

    for s, expected in test_cases:
        res = is_balanced(s)
        status = "[OK]" if res == expected else "[FAIL]"
        print(f"{status} '{s}' -> Balanced? {res} | Expected: {expected}")
        assert res == expected, f"Failed for '{s}'"

    print("\n[PASS] All Balanced Parentheses tests passed successfully!")
