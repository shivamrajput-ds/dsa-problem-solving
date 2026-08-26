# Day 03 — Strings + Frequency Counting

## Problems Solved

### 1. Codeforces — B. Dubstep

**Approach:**

* Read the remix string.
* Split the string using `"WUB"` as the separator.
* `split("WUB")` may generate empty strings when:

  * `"WUB"` occurs at the beginning,
  * `"WUB"` occurs at the end,
  * multiple `"WUB"` blocks occur consecutively.
* Filter out all empty strings.
* Join the remaining words using a single space.

**Important Observation:**

```text
Input:
WUBWUBABCWUBDEFWUB

After split("WUB"):

["", "", "ABC", "DEF", ""]

After removing empty strings:

["ABC", "DEF"]

Final:

ABC DEF
```

**Key Learning:**

* `split()` breaks a string into parts using a separator.
* Splitting can create empty strings at boundaries or between consecutive separators.
* Python strings are immutable.
* Instead of repeatedly concatenating strings, collect words in a list and use `" ".join(...)` once.
* `join()` is useful when constructing a final string from multiple pieces.

**Complexity:**

* Time: `O(n)`
* Space: `O(n)`

where `n` is the length of the remix string.

---

### 2. Codeforces — A. Amusing Joke

**Approach:**

* Create a frequency map.
* Add frequencies of every character from the guest name.
* Add frequencies of every character from the host name.
* For every character in the pile, decrease its frequency.
* Finally check whether every frequency is exactly `0`.
* If every count becomes `0`, print `YES`; otherwise print `NO`.

**Important Observation:**

It is not enough to check only whether the pile contains extra characters.

Example:

```text
Guest + Host:
ABC

Pile:
AB
```

After processing:

```text
A → 0
B → 0
C → 1
```

There is no extra character in the pile, but `C` is missing.

Therefore, the final condition must be:

```text
Every frequency == 0
```

**Key Learning:**

* Frequency maps are useful for checking whether two collections contain exactly the same elements with the same counts.
* A dictionary's space complexity depends on how many unique keys it can contain.
* Since the problem contains only uppercase English letters, there can be at most `26` frequency entries.
* Therefore the frequency map itself uses constant auxiliary space.

**Complexity:**

Let:

* `m` = length of guest name
* `n` = length of host name
* `p` = length of pile

Time:

```text
Guest traversal → O(m)
Host traversal  → O(n)
Pile traversal  → O(p)
Frequency check → O(26) = O(1)

Total → O(m + n + p)
```

Auxiliary space for the frequency map:

```text
Maximum unique characters = 26

Space → O(1)
```

---

## Today's Main Learnings

* String splitting
* Filtering empty strings
* Efficient string construction using `join()`
* Python string immutability
* Frequency counting with `defaultdict`
* Exact frequency matching
* Understanding fixed-alphabet space complexity
* Distinguishing input size from number of possible unique keys

---

## Problems Completed

| Problem      | Platform   | Status |
| ------------ | ---------- | ------ |
| Dubstep      | Codeforces | ✅      |
| Amusing Joke | Codeforces | ✅      |

---

## Day 03 Takeaway

> A correct solution is not only about finding the right data structure — small details in how data is transformed also matter.

For **Dubstep**, the important detail was handling empty strings created by `split()`.

For **Amusing Joke**, the important detail was ensuring every final character frequency becomes exactly `0`.
