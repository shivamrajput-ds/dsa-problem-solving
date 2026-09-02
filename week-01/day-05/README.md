# Day 05 — One-Pass Optimization + Frequency Counting

## Problems Solved

### 1. LeetCode 121 — Best Time to Buy and Sell Stock

**Approach:**

* Keep track of the minimum stock price seen so far using `min_price`.
* Traverse the prices from left to right.
* If a smaller price is found, update `min_price`.
* Otherwise, calculate the profit if the stock is sold at the current price.
* Keep track of the maximum profit found so far.

**Important Observation:**

For every possible selling day, the best buying price is the minimum price seen before that day.

```text
Current Profit = Current Price - Minimum Price Seen So Far
```

This allows the problem to be solved in one pass without checking every pair of days.

**Key Learning:**

* Maintain useful information from previously processed elements.
* Avoid brute-force comparison of every buy/sell pair.
* A running minimum can help convert an `O(n²)` idea into an `O(n)` solution.
* Variable names such as `min_price` and `max_profit` make the algorithm easier to understand.

**Complexity:**

* Time: `O(n)`
* Space: `O(1)`

---

### 2. LeetCode 242 — Valid Anagram

I solved this problem using **two different approaches**.

---

#### Approach 1 — Fixed Frequency Array

**Approach:**

* Since the problem contains only lowercase English letters, create a frequency array of size `26`.
* Increase the frequency for every character in `s`.
* Decrease the frequency for every character in `t`.
* Finally, verify that every frequency is `0`.

**Important Observation:**

The constraints guarantee only:

```text
a-z
```

Therefore, there are exactly `26` possible character positions.

A character can be mapped to an index using:

```python
ord(ch) - ord("a")
```

**Key Learning:**

* Always use constraints when choosing a data structure.
* A fixed alphabet can be represented efficiently using an array.
* `ord()` can convert characters into numeric Unicode code points.
* `O(26)` auxiliary space simplifies to `O(1)`.

**Complexity:**

* Time: `O(n + m)`
* Space: `O(1)`

---

#### Approach 2 — Hash Map / defaultdict

**Approach:**

* First check whether both strings have the same length.
* Store character frequencies of `s` in a dictionary.
* Traverse `t` and decrease the corresponding frequencies.
* If any frequency becomes negative, immediately return `False`.
* If the traversal completes successfully, return `True`.

**Important Observation:**

Unlike the fixed array approach, a dictionary is not restricted to only `a-z`.

This makes the same idea easier to adapt when the input may contain a larger set of characters, including Unicode characters.

**Key Learning:**

* Hash maps are useful when the possible key space is not fixed.
* Dictionary space depends on the number of unique keys, not simply the total input length.
* Early termination can avoid unnecessary work when a mismatch is detected.
* Fixed arrays and hash maps can solve the same frequency-counting problem with different trade-offs.

**Complexity:**

Let:

```text
n = len(s)
m = len(t)
k = number of unique characters
```

* Time: `O(n + m)`
* Space: `O(k)`

In the worst case, `k` may grow with the input size.

---

## Complexity Summary

| Problem / Approach              | Time Complexity | Space Complexity |
| ------------------------------- | --------------- | ---------------- |
| Best Time to Buy and Sell Stock | `O(n)`          | `O(1)`           |
| Valid Anagram — Frequency Array | `O(n + m)`      | `O(1)`           |
| Valid Anagram — Hash Map        | `O(n + m)`      | `O(k)`           |

---

## Today's Main Learnings

* One-pass optimization
* Maintaining a running minimum
* Avoiding unnecessary nested loops
* Frequency counting
* Using constraints to select a data structure
* Fixed-size arrays vs hash maps
* Character indexing using `ord()`
* Unicode-aware thinking
* Understanding that hash-map space depends on unique keys
* Early termination when a mismatch is detected

---

## Problems Completed

| Problem                         | Platform | Status |
| ------------------------------- | -------- | ------ |
| Best Time to Buy and Sell Stock | LeetCode | ✅      |
| Valid Anagram                   | LeetCode | ✅      |

---

## Day 05 Takeaway

> Before choosing a data structure, look carefully at the constraints.

For **Best Time to Buy and Sell Stock**, maintaining the minimum value seen so far removed the need for brute force.

For **Valid Anagram**, the fixed `a-z` constraint allowed an `O(1)` frequency array, while the hash-map approach provided a more general solution for larger character sets.
