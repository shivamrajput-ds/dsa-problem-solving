# Day 04 — Sorting + Kadane's Algorithm

## Problems Solved

### 1. Distinct Numbers — CSES

**Goal:** Count how many distinct values are present in the input array.

**Approach:**
- Sort the array.
- The first element is always counted as distinct.
- Scan from left to right.
- Whenever the current value differs from the last distinct value, increment the count.

**Complexity:**
- Time: `O(n log n)` because sorting dominates the linear scan.
- Auxiliary Space: Python's built-in `sort()` may use up to `O(n)` extra memory in the worst case.

**Key Learning:**
- Sorting makes equal values adjacent, which makes duplicate detection simple.
- An `O(n log n)` sorting solution can be more predictable than hashing on adversarial inputs.

---

### 2. Maximum Subarray Sum — Kadane's Algorithm

**Goal:** Find the maximum possible sum of a contiguous subarray.

**Approach:**
- Maintain a running sum.
- Add each value to the running sum.
- Update the best sum seen so far.
- If the running sum becomes negative, reset it to `0` because a negative prefix cannot help a future subarray.

**Complexity:**
- Time: `O(n)`
- Auxiliary Space: `O(1)`

**Key Learning:**
- A negative running prefix should be discarded.
- Initializing the answer with `-inf` correctly handles arrays containing only negative values.

---

## What I Practiced

- Sorting and scanning adjacent values
- Distinct-element counting
- Kadane's Algorithm
- Running-state optimization
- Handling all-negative arrays
- Time and space complexity analysis

## Important Observations

- `split()` is cleaner than `split(" ")` for competitive-programming input because it handles arbitrary whitespace.
- A redundant `continue` at the end of a loop body can be removed.
- Variable names should describe their role, such as `last_seen` instead of a generic `seen`.
- In Kadane's Algorithm, update `max_sum` before resetting a negative running sum.

## Folder Structure

```text
week-01/
└── day-04/
    ├── distinct_numbers.py
    ├── maximum_subarray_sum.py
    └── README.md
```
