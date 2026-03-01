# Design

## Part 1 - Ordinary Sets
Representation: Boolean array
Operations:
- NOT(A): Flip all values
- Union: OR operation
- Intersection: AND operation
- Difference: A AND NOT B
- Symmetric Difference: (A-B) U (B-A)

## Part 2 - Multisets
Representation: Map (element -> count)

Operations:
- Union: max(countA, countB)
- Intersection: min(countA, countB)
- Difference: max(countA - countB, 0)
- Sum: countA + countB
