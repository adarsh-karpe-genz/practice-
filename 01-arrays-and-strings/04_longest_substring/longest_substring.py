"""
Problem: Longest Substring Without Repeating Characters
LeetCode: #3 (Medium)

Approach: Sliding Window with Hash Map
Time Complexity: O(N)
Space Complexity: O(min(N, charset))
"""

def length_of_longest_substring(s: str) -> int:
    char_index = {}
    max_len = 0
    left = 0

    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        char_index[char] = right
        max_len = max(max_len, right - left + 1)

    return max_len

if __name__ == "__main__":
    print("[Python] Longest Substring Test")
    tests = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
    ]
    for s, expected in tests:
        res = length_of_longest_substring(s)
        print(f"s: '{s}' -> Max Len: {res} | Expected: {expected}")
        assert res == expected
    print("All Longest Substring tests passed!")
