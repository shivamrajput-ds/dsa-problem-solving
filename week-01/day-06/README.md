# Day 06 — Sliding Window + Prefix Sum

## Problems Solved

### 1. Codeforces — B. Fence

**Approach:**

* Calculate the sum of the first `k` fence heights.
* Treat it as the current sliding window sum.
* Move the window one position at a time.
* Remove the element leaving the window.
* Add the new element entering the window.
* Track the minimum window sum and its starting position.
* Convert the result to a 1-based index before printing.

**Important Observation:**

Recalculating the sum of every block of `k` elements would repeat a lot of work.

Instead:

```text
New Window Sum
= Previous Window Sum
- Element Leaving
+ Element Entering
```

This allows every new window to be processed in constant time.

**Key Learning:**

* Sliding window is useful when working with consecutive fixed-size ranges.
* Reusing the previous window result avoids repeated calculations.
* Index conversion between 0-based Python indexing and 1-based problem output must be handled carefully.
* Repeated range calculations can often be optimized by maintaining only the changing part.

**Complexity:**

* Time: `O(n)`
* Auxiliary Space: `O(1)`

The input array itself requires `O(n)` memory.

---

### 2. Codeforces — C. Kuriyama Mirai's Stones

**Approach:**

* Keep the original array for type `1` queries.
* Create a sorted copy for type `2` queries.
* Build one prefix-sum array for the original order.
* Build another prefix-sum array for the sorted order.
* Use prefix arrays of size `n + 1`.
* Answer every range-sum query in `O(1)`.

For a range `[l, r]`:

```text
Range Sum = prefix[r] - prefix[l - 1]
```

**Important Observation:**

Without prefix sums, calculating every query by traversing from `l` to `r` could take `O(n)` per query.

With prefix sums:

```text
Preprocessing → done once
Each query   → O(1)
```

Using a prefix array of size `n + 1` also avoids a special case when:

```text
l = 1
```

because:

```text
prefix[0] = 0
```

**Key Learning:**

* Prefix sums are useful when many range-sum queries are asked on the same data.
* Precomputation can trade additional memory for much faster queries.
* Sometimes multiple versions of the same data require separate prefix arrays.
* A prefix array of size `n + 1` makes range-sum formulas cleaner.
* Sorting must also be included when deriving the total complexity.

**Complexity:**

```text
Sorting          → O(n log n)
Prefix Building  → O(n)
m Queries        → O(m)
```

Therefore:

* Time: `O(n log n + m)`
* Space: `O(n)`

---

## Complexity Summary

| Problem                 | Time Complexity  | Auxiliary Space |
| ----------------------- | ---------------- | --------------- |
| Fence                   | `O(n)`           | `O(1)`          |
| Kuriyama Mirai's Stones | `O(n log n + m)` | `O(n)`          |

---

## Today's Main Learnings

* Fixed-size sliding window
* Reusing previous computations
* Removing the outgoing element and adding the incoming element
* Prefix-sum preprocessing
* `n + 1` prefix-array technique
* Constant-time range-sum queries
* Maintaining prefix sums for original and sorted arrays
* Including preprocessing, sorting, and queries in total complexity analysis
* Careful handling of 0-based and 1-based indexing

---

## Mistakes / Important Observations

* In **Fence**, recalculating every window sum from scratch would do unnecessary repeated work.
* The answer required a **1-based starting index**, while Python uses 0-based indexing.
* In **Kuriyama Mirai's Stones**, there are two different query types, so both the original and sorted arrays need separate prefix sums.
* Using `prefix[0] = 0` removes the need to handle `l = 1` separately.
* Query processing must be included in the final complexity, giving `O(n log n + m)` rather than only `O(n log n)`.

---

## Problems Completed

| Problem                 | Platform   | Status |
| ----------------------- | ---------- | ------ |
| Fence                   | Codeforces | ✅      |
| Kuriyama Mirai's Stones | Codeforces | ✅      |

---

## Day 06 Takeaway

> When the same calculation is being repeated, ask whether the previous result can be reused or whether some information can be precomputed.

In **Fence**, the previous window sum was reused using a sliding window.

In **Kuriyama Mirai's Stones**, range sums were precomputed using prefix sums so that each query could be answered in `O(1)`.
