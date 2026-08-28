# 🚀 Problem Solving & Data Structures (DSA) Repository

[![Language-C](https://img.shields.io/badge/Language-C-blue.svg)](https://en.wikipedia.org/wiki/C_(programming_language))
[![Language-C++](https://img.shields.io/badge/Language-C%2B%2B-00599C.svg)](https://isocpp.org/)
[![Language-Java](https://img.shields.io/badge/Language-Java-ED8B00.svg)](https://www.java.com/)
[![Language-Python](https://img.shields.io/badge/Language-Python-3776AB.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Active%20Practicing-success.svg)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)]()

A curated, production-quality collection of **Data Structures, Algorithms, and Problem-Solving patterns** implemented across **C, C++, Java, and Python**. Designed for Second-Year (SY) engineering students, competitive programmers, and technical interview preparation.

---

## 📂 Repository Structure

```tree
practice/
├── 01-arrays-and-strings/
│   ├── 01_two_sum/
│   ├── 02_kadanes_algorithm/
│   ├── 03_trapping_rain_water/
│   └── 04_longest_substring/
├── 02-linked-lists/
│   ├── 01_reverse_linked_list/
│   ├── 02_merge_two_sorted_lists/
│   └── 03_detect_cycle/
├── 03-searching-and-sorting/
│   ├── 01_binary_search/
│   ├── 02_merge_sort/
│   └── 03_quick_sort/
├── 04-trees-and-graphs/
│   ├── 01_binary_tree_traversals/
│   ├── 02_lowest_common_ancestor/
│   └── 03_bfs_dfs_graph/
├── 05-dynamic-programming/
│   ├── 01_climbing_stairs/
│   ├── 02_coin_change/
│   └── 03_longest_common_subsequence/
└── 06-math-and-bit-manipulation/
    ├── 01_sieve_of_eratosthenes/
    └── 02_single_number/
```

---

## 📊 Problem Index & Complexity Cheat Sheet

| # | Category | Problem Name | Difficulty | Time Complexity | Space Complexity | Implementations |
|---|---|---|---|---|---|---|
| 01 | Arrays & Strings | Two Sum | 🟢 Easy | $O(N)$ | $O(N)$ | [C](01-arrays-and-strings/01_two_sum/two_sum.c) · [C++](01-arrays-and-strings/01_two_sum/two_sum.cpp) · [Java](01-arrays-and-strings/01_two_sum/TwoSum.java) · [Python](01-arrays-and-strings/01_two_sum/two_sum.py) |
| 02 | Arrays & Strings | Kadane's Algorithm (Max Subarray) | 🟡 Medium | $O(N)$ | $O(1)$ | [C](01-arrays-and-strings/02_kadanes_algorithm/kadanes_algorithm.c) · [C++](01-arrays-and-strings/02_kadanes_algorithm/kadanes_algorithm.cpp) · [Java](01-arrays-and-strings/02_kadanes_algorithm/KadanesAlgorithm.java) · [Python](01-arrays-and-strings/02_kadanes_algorithm/kadanes_algorithm.py) |
| 03 | Arrays & Strings | Trapping Rain Water | 🔴 Hard | $O(N)$ | $O(1)$ | [C](01-arrays-and-strings/03_trapping_rain_water/trapping_rain_water.c) · [C++](01-arrays-and-strings/03_trapping_rain_water/trapping_rain_water.cpp) · [Java](01-arrays-and-strings/03_trapping_rain_water/TrappingRainWater.java) · [Python](01-arrays-and-strings/03_trapping_rain_water/trapping_rain_water.py) |
| 04 | Arrays & Strings | Longest Substring Without Repeating | 🟡 Medium | $O(N)$ | $O(\min(N, \Sigma))$ | [C](01-arrays-and-strings/04_longest_substring/longest_substring.c) · [C++](01-arrays-and-strings/04_longest_substring/longest_substring.cpp) · [Java](01-arrays-and-strings/04_longest_substring/LongestSubstring.java) · [Python](01-arrays-and-strings/04_longest_substring/longest_substring.py) |
| 05 | Linked Lists | Reverse Linked List | 🟢 Easy | $O(N)$ | $O(1)$ | [C](02-linked-lists/01_reverse_linked_list/reverse_linked_list.c) · [C++](02-linked-lists/01_reverse_linked_list/reverse_linked_list.cpp) · [Java](02-linked-lists/01_reverse_linked_list/ReverseLinkedList.java) · [Python](02-linked-lists/01_reverse_linked_list/reverse_linked_list.py) |
| 06 | Linked Lists | Merge Two Sorted Lists | 🟢 Easy | $O(N + M)$ | $O(1)$ | [C](02-linked-lists/02_merge_two_sorted_lists/merge_two_sorted_lists.c) · [C++](02-linked-lists/02_merge_two_sorted_lists/merge_two_sorted_lists.cpp) · [Java](02-linked-lists/02_merge_two_sorted_lists/MergeSortedLists.java) · [Python](02-linked-lists/02_merge_two_sorted_lists/merge_two_sorted_lists.py) |
| 07 | Linked Lists | Detect Cycle (Floyd's Algorithm) | 🟢 Easy | $O(N)$ | $O(1)$ | [C](02-linked-lists/03_detect_cycle/detect_cycle.c) · [C++](02-linked-lists/03_detect_cycle/detect_cycle.cpp) · [Java](02-linked-lists/03_detect_cycle/DetectCycle.java) · [Python](02-linked-lists/03_detect_cycle/detect_cycle.py) |
| 08 | Searching & Sorting | Binary Search | 🟢 Easy | $O(\log N)$ | $O(1)$ | [C](03-searching-and-sorting/01_binary_search/binary_search.c) · [C++](03-searching-and-sorting/01_binary_search/binary_search.cpp) · [Java](03-searching-and-sorting/01_binary_search/BinarySearch.java) · [Python](03-searching-and-sorting/01_binary_search/binary_search.py) |
| 09 | Searching & Sorting | Merge Sort | 🟡 Medium | $O(N \log N)$ | $O(N)$ | [C](03-searching-and-sorting/02_merge_sort/merge_sort.c) · [C++](03-searching-and-sorting/02_merge_sort/merge_sort.cpp) · [Java](03-searching-and-sorting/02_merge_sort/MergeSort.java) · [Python](03-searching-and-sorting/02_merge_sort/merge_sort.py) |
| 10 | Searching & Sorting | Quick Sort | 🟡 Medium | $O(N \log N)$ avg | $O(\log N)$ | [C](03-searching-and-sorting/03_quick_sort/quick_sort.c) · [C++](03-searching-and-sorting/03_quick_sort/quick_sort.cpp) · [Java](03-searching-and-sorting/03_quick_sort/QuickSort.java) · [Python](03-searching-and-sorting/03_quick_sort/quick_sort.py) |
| 11 | Trees & Graphs | Binary Tree Traversals (BFS/DFS) | 🟢 Easy | $O(N)$ | $O(H) / O(W)$ | [C](04-trees-and-graphs/01_binary_tree_traversals/binary_tree_traversals.c) · [C++](04-trees-and-graphs/01_binary_tree_traversals/binary_tree_traversals.cpp) · [Java](04-trees-and-graphs/01_binary_tree_traversals/BinaryTreeTraversals.java) · [Python](04-trees-and-graphs/01_binary_tree_traversals/binary_tree_traversals.py) |
| 12 | Trees & Graphs | Lowest Common Ancestor (LCA) | 🟡 Medium | $O(N)$ | $O(H)$ | [C](04-trees-and-graphs/02_lowest_common_ancestor/lowest_common_ancestor.c) · [C++](04-trees-and-graphs/02_lowest_common_ancestor/lowest_common_ancestor.cpp) · [Java](04-trees-and-graphs/02_lowest_common_ancestor/LowestCommonAncestor.java) · [Python](04-trees-and-graphs/02_lowest_common_ancestor/lowest_common_ancestor.py) |
| 13 | Trees & Graphs | Graph Traversals (BFS & DFS) | 🟡 Medium | $O(V + E)$ | $O(V + E)$ | [C](04-trees-and-graphs/03_bfs_dfs_graph/bfs_dfs_graph.c) · [C++](04-trees-and-graphs/03_bfs_dfs_graph/bfs_dfs_graph.cpp) · [Java](04-trees-and-graphs/03_bfs_dfs_graph/GraphTraversals.java) · [Python](04-trees-and-graphs/03_bfs_dfs_graph/bfs_dfs_graph.py) |
| 14 | Dynamic Programming | Climbing Stairs | 🟢 Easy | $O(N)$ | $O(1)$ | [C](05-dynamic-programming/01_climbing_stairs/climbing_stairs.c) · [C++](05-dynamic-programming/01_climbing_stairs/climbing_stairs.cpp) · [Java](05-dynamic-programming/01_climbing_stairs/ClimbingStairs.java) · [Python](05-dynamic-programming/01_climbing_stairs/climbing_stairs.py) |
| 15 | Dynamic Programming | Coin Change | 🟡 Medium | $O(	ext{Amount} \cdot N)$ | $O(	ext{Amount})$ | [C](05-dynamic-programming/02_coin_change/coin_change.c) · [C++](05-dynamic-programming/02_coin_change/coin_change.cpp) · [Java](05-dynamic-programming/02_coin_change/CoinChange.java) · [Python](05-dynamic-programming/02_coin_change/coin_change.py) |
| 16 | Dynamic Programming | Longest Common Subsequence | 🟡 Medium | $O(M \cdot N)$ | $O(M \cdot N)$ | [C](05-dynamic-programming/03_longest_common_subsequence/lcs.c) · [C++](05-dynamic-programming/03_longest_common_subsequence/lcs.cpp) · [Java](05-dynamic-programming/03_longest_common_subsequence/LongestCommonSubsequence.java) · [Python](05-dynamic-programming/03_longest_common_subsequence/lcs.py) |
| 17 | Math & Bitwise | Sieve of Eratosthenes | 🟢 Easy | $O(N \log \log N)$ | $O(N)$ | [C](06-math-and-bit-manipulation/01_sieve_of_eratosthenes/sieve.c) · [C++](06-math-and-bit-manipulation/01_sieve_of_eratosthenes/sieve.cpp) · [Java](06-math-and-bit-manipulation/01_sieve_of_eratosthenes/SieveOfEratosthenes.java) · [Python](06-math-and-bit-manipulation/01_sieve_of_eratosthenes/sieve.py) |
| 18 | Math & Bitwise | Single Number (Bitwise XOR) | 🟢 Easy | $O(N)$ | $O(1)$ | [C](06-math-and-bit-manipulation/02_single_number/single_number.c) · [C++](06-math-and-bit-manipulation/02_single_number/single_number.cpp) · [Java](06-math-and-bit-manipulation/02_single_number/SingleNumber.java) · [Python](06-math-and-bit-manipulation/02_single_number/single_number.py) |

---

## 🛠️ How to Compile & Run

### 1. C
```bash
gcc 01-arrays-and-strings/01_two_sum/two_sum.c -o two_sum.exe
./two_sum.exe
```

### 2. C++
```bash
g++ -std=c++17 01-arrays-and-strings/01_two_sum/two_sum.cpp -o two_sum.exe
./two_sum.exe
```

### 3. Java
```bash
javac 01-arrays-and-strings/01_two_sum/TwoSum.java
java -cp 01-arrays-and-strings/01_two_sum TwoSum
```

### 4. Python
```bash
python 01-arrays-and-strings/01_two_sum/two_sum.py
```

---

## 🎯 Contribution & Practice Routine

1. **Pick a problem** from the index table.
2. **Solve it in your primary language** first (e.g., C++ or Java).
3. **Re-implement in Python** for quick prototyping or **C** for memory/pointer mastery.
4. **Commit daily** to maintain consistent learning and keep your GitHub contribution graph active! 🟩

```bash
git add .
git commit -m "feat: add multi-language DSA problem solutions"
git push origin main
```

---

*Authored with ❤️ for problem solving & engineering excellence.*
