# Patterns

## Grid chunking / 2D-to-1D indexing

**Recognize:** problem partitions a 2D grid into fixed-size blocks (sudoku boxes,
image patches, matrix tiles) and needs per-block state.

**Pattern:**
- Cell (i, j) in k×k chunks → chunk coords = (i // k, j // k)
- Flatten to 1D index → (i // k) * (num_chunks_per_row) + (j // k)

**Seen in:** Valid Sudoku (k=3, 9 boxes flattened to indices 0–8)

**Bug watch:** off-by-one on `num_chunks_per_row` vs `num_cols`. They're equal
only when the grid is exactly k×k chunks wide. Tabulate 2–3 (i, j) → index
mappings before trusting the formula.


## Set + chain walking (NOT sliding window)

**Recognize:** "longest consecutive / sequential / chain" over an *unsorted*
collection where elements don't need to be contiguous in the input. The O(n)
requirement rules out sort.

**Pattern:**
1. Dump everything into a set (O(1) lookup).
2. Iterate the set. For each element `n`, check if `n - 1` is in the set.
3. If `n - 1` is absent, `n` is a chain-start → walk forward (`n+1`, `n+2`, ...)
   counting length until you fall off.
4. Track global max.

**Why O(n):** every element is touched at most twice — once by the outer scan,
once by exactly one inner walk (the walk that starts at its chain's head). The
nested loop looks like O(n²) but is amortized O(n). Have this sentence ready
for interviewers.

**Seen in:** LeetCode 128 Longest Consecutive Sequence

**Bug watch:**
- Iterate the *set*, not the input list, or duplicates do redundant work.
- The chain-start check is `n - 1 not in set`, not `n + 1 not in set`.


## Two Pointers

1. Three types, by configuration:

Opposite ends → pointers at [0, n-1], move inward
Fast/slow → both start left, fast moves quicker
Two sequences → one pointer per array

2. When you see one:

Sorted array + looking for a pair → opposite ends
In-place array edit or cycle → fast/slow
Merging two sorted things → two sequences

3. The one question that gives you the move rule:

Which pointer, if I keep it, can never beat what I've already seen?

Move that one.
4. Termination check:
Every loop iteration must move some pointer. If a code path doesn't, you have an infinite loop.


![alt text](image.png)


## Stacks — core idea

**Mantra:** *Last in, first out. The most recent unresolved thing is the next
to handle.*

**Recognize:** problems involve nesting, matching, or "what came right before
this matters." Validity depends on most recent context. Or: "for each X, find
the next/previous greater/smaller X."

**In Python:** just use a list. `append()` = push, `pop()` = pop, `[-1]` = peek.
All O(1). No imports.

**Sub-patterns below:** bracket matching, monotonic stack, parallel/auxiliary
stack. Backtracking is a separate entry — uses a stack but is conceptually
distinct.


## Bracket matching / parser style

**Recognize:** validity depends on properly nested pairs (brackets, tags,
expressions). Every opener creates an obligation; every closer must resolve
the most recent open obligation.

**Pattern:**
1. Opener → push.
2. Closer → check top; if it matches the expected opener → pop. Else fail.
3. End → stack must be empty for validity.

**Seen in:** Valid Parentheses (LC 20).

**Bug watch:**
- Popping from empty stack → check `stack` is truthy before popping.
- Forgetting the final "stack empty?" check (open brackets with no matching
  close).
- Defensive `.get(key, None)` when direct indexing is correct — inside the
  closer branch, the char is guaranteed to be in the closer→opener dict.


## Monotonic stack

**Mantra:** *Stack holds unresolved questions in order. The answer arrives
when the invariant breaks.*

**Recognize:** "for each element, find the next/previous greater/smaller
element." Or arrival-time / dominance / span problems where the answer to
question `j` is the first later element that beats `j`.

**Pattern (next greater, iterating L→R):**

```python
stack = []   # store INDICES, not values
for i in range(len(arr)):
    while stack and arr[i] > arr[stack[-1]]:
        j = stack.pop()
        result[j] = i - j   # or whatever the question asks
    stack.append(i)
```

**Direction rules:**
- Next greater → iterate L→R, stack stays decreasing
- Next smaller → iterate L→R, stack stays increasing
- Previous greater/smaller → iterate R→L, flip accordingly

**Why O(n):** every index is pushed and popped at most once across the entire
run. The nested `while` is amortized O(1) per outer step. Have this sentence
ready for interviewers — "amortized" is the keyword.

**Seen in:**
- Daily Temperatures (LC 739) — classic monotonic decreasing stack of indices.
- Car Fleet (LC 853) — sort cars by position descending; push arrival times;
  push only when `t_new > stack[-1]`. Stack stays strictly increasing in
  arrival time. Answer = `len(stack)`.

**Bug watch:**
- Push indices, not values, when positional info matters (distance, span).
- Strict vs non-strict comparison (`<` vs `<=`). Depends on whether ties count
  as the same fleet / same group. **State the boundary case out loud before
  writing the comparison.** This is my recurring bug — flagged.
- Forgetting to push the current index *after* the while loop.


## Parallel / auxiliary stack

**Recognize:** need O(1) access to a derived property (min, max, running sum)
at every state of a primary stack.

**Pattern:** maintain a side stack in lockstep with the main stack. On every
push to main, push the derived property to side. On every pop from main, pop
from side.

For min: on each push, append `min(val, side[-1] if side else val)` to side.
Top of side is always the current min.

**Seen in:** Min Stack (LC 155).

**Bug watch:**
- Don't try to keep the side stack sorted. It doesn't need to be. It only
  needs to answer "what's the current min" at this level.
- Pop in lockstep. Easy to forget the side pop on main pop.


## Backtracking (uses a stack, conceptually distinct from above)

**Mantra:** *Choose → recurse → unchoose.*

**Recognize:** generate all valid configurations (subsets, permutations,
combinations, all paths, all valid strings) under some constraint. Different
from monotonic stack / bracket matching — this is tree search with a path you
build incrementally.

**Pattern:**

```python
def backtrack(state):
    if base_case(state):
        results.append(snapshot(path))
        return
    for choice in choices_given(state):
        if valid(choice, state):
            path.append(choice)
            backtrack(updated_state)
            path.pop()        # undo — critical
```

**Critical discipline:** every `path.append(...)` must be paired with a
`path.pop()` *immediately after* the corresponding recursive call returns.
The pop undoes the choice so the next iteration starts from clean state. Do
not consolidate pops at the bottom of the function.

**Seen in:** Generate Parentheses (LC 22). State = `(num_open, num_close)`.
Rules: add `(` if `num_open < n`; add `)` if `num_close < num_open`.

**Bug watch:**
- **Missing `return` after base case** → execution falls through and may
  re-recurse on the wrong branches. Doesn't always break correctness but
  always wastes work.
- **Single bottom-of-function `pop()`** instead of paired pops per branch.
  Pops must match appends 1:1, branch by branch.
- **Tracking the wrong state.** Generate Parens needs `(open, close)`, not
  just `pairs` — the two counts are independent constraints.
- **Forgetting to actually append the choice** before recursing. Silently
  recurses on the wrong state.

**Time complexity heuristic:** branching factor `b`, depth `d` → loose upper
bound is `O(b^d)` × work per leaf. For Generate Parens: `b=2`, `d=2n`, leaf
work = O(n) to build the string → `O(n · 4^n)`. Tighter bound is `4^n / √n`
via Catalan, but the loose bound is easier to derive and defend.
