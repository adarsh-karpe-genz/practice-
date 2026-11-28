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

Time Complexity: O(N)
Space Complexity: O(N) for the stack
"""

def is_balanced(s: str) -> bool:
    """Checks if parentheses are balanced using a stack."""
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []
    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
    return len(stack) == 0


def max_nesting_depth(s: str) -> int:
    """Calculates maximum nesting depth of parentheses."""
    depth = 0
    max_d = 0
    for char in s:
        if char in '({[':
            depth += 1
            max_d = max(max_d, depth)
        elif char in ')}]':
            depth = max(0, depth - 1)
    return max_d


def min_removals_to_make_valid(s: str) -> int:
    """
    Calculates minimum number of parentheses that must be removed
    to make the string valid/balanced. (Handles '(' and ')' pairs).
    """
    open_count = 0
    invalid_close = 0
    for ch in s:
        if ch == '(':
            open_count += 1
        elif ch == ')':
            if open_count > 0:
                open_count -= 1
            else:
                invalid_close += 1
    return open_count + invalid_close


if __name__ == "__main__":
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("(((", False),
        ("])}", False),
        ("{[()]}", True),
    ]

    for s, expected in test_cases:
        res = is_balanced(s)
        assert res == expected, f"Failed for '{s}'"
    assert max_nesting_depth("((()))") == 3
    assert max_nesting_depth("{[()]}") == 3

    # Test min removals
    assert min_removals_to_make_valid("())") == 1
    assert min_removals_to_make_valid("(((") == 3
    assert min_removals_to_make_valid("()()") == 0

    print("[PASS] Problem 26: Balanced Parentheses tests passed successfully!")
