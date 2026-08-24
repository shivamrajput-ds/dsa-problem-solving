# Day 01 — Implementation + Basic Math

## Problems Solved

### 1. Codeforces — Beautiful Matrix

**Approach:**

* Read the complete `5 x 5` matrix.
* Find the position of `1`.
* Target position is the center `(2, 2)` using 0-based indexing.
* Calculate the number of moves using row distance + column distance.

**Key Learning:**

* Practiced 2D matrix traversal.
* Used early `break` after finding the required element.
* Understood how row and column movement can be calculated independently.
* Practiced using absolute distance with `abs()`.

---

### 2. Codeforces — Theatre Square

**Approach:**

* Find how many flagstones are required along the length.
* Find how many flagstones are required along the width.
* Multiply both counts.

```text
required rows × required columns
```

**Key Learning:**

* Converted a geometry-looking problem into a simple mathematical observation.
* Understood why partial remaining space still requires one complete flagstone.
* Practiced ceiling division using `math.ceil()`.

---

## Today's Main Learning

* Clean implementation
* Matrix traversal
* Breaking nested search efficiently
* Manhattan-style row/column distance
* Ceiling division
* Converting problem statements into simple mathematical formulas

## Status

* Beautiful Matrix ✅
* Theatre Square ✅

Both problems solved with proper understanding instead of only chasing Accepted submissions.
