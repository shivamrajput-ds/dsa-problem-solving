# Day 02 — Counting, Sorting Logic & Simulation

## Problems Solved

### 1. Codeforces — A. Helpful Maths

**Approach:**

* Split the expression using `"+"`.
* Count the number of `1`s, `2`s, and `3`s.
* Rebuild the expression in sorted order.
* Join the result using `"+"`.

**Key Learning:**

* Sorting is not always necessary when the possible values are very limited.
* Frequency counting can sometimes replace comparison-based sorting.
* Multiple loops can still combine to `O(n)` if the total number of iterations remains proportional to the input size.

**Complexity:**

* Time: `O(n)`
* Space: `O(n)`

---

### 2. Codeforces — B. Queue at the School

**Approach:**

* Convert the string into a list because Python strings are immutable.
* Simulate the queue for `t` seconds.
* Whenever `BG` appears, swap it to `GB`.
* After a swap, move the index by `2` so the same boy is not processed again during the same second.

**Important Observation:**

```text
Before:
B G G

After one valid swap:
G B G

The newly moved B must NOT move again
during the same second.

Therefore:
i += 2
```

**Key Learning:**

* Simulation problems require following the exact timing/order described in the statement.
* Updating the loop index correctly can be essential for correctness.
* A locally correct swap can still produce a wrong answer if the updated state is processed too early.

**Complexity:**

* Time: `O(t × n)`
* Space: `O(n)`

---

## Today's Main Learnings

* Frequency counting
* Simple sorting logic
* Simulation
* Mutable vs immutable data in Python
* Careful index movement after state changes
* Deriving time complexity from total loop iterations
* Understanding that consecutive loops do not automatically multiply complexities

---

## Problems Completed

| Problem             | Platform   | Status |
| ------------------- | ---------- | ------ |
| Helpful Maths       | Codeforces | ✅      |
| Queue at the School | Codeforces | ✅      |

---

## Day 02 Takeaway

> Do not only ask, "Does my code work?"

Also ask:

> "Why does this update happen now, and should the modified element be processed again?"

This was especially important in **Queue at the School**.
