# CS2430 Programming Project 1
# Sets, Multisets, and Natural-Language Data Queries
# Hanseo Yun

# =====================================================
# PART 1: Ordinary Sets (Boolean Arrays)
# =====================================================

U = ["A","B","C","D","E","F","G","H","I","J"]

def _validate_bool_array(bool_array):
    if len(bool_array) != len(U):
        raise ValueError(f"Boolean array length must match universe size {len(U)}.")

def _to_bitstring(bool_array):
    return "".join("1" if x else "0" for x in bool_array)

def print_set(name, bool_array):
    _validate_bool_array(bool_array)
    elements = [U[i] for i in range(len(U)) if bool_array[i]]
    print(f"{name} (bool)     : {bool_array}")
    print(f"{name} (bitstring): {_to_bitstring(bool_array)}")
    print(f"{name} (elements) : {elements}")
    print()

def complement(A):
    _validate_bool_array(A)
    return [not x for x in A]

def union(A, B):
    _validate_bool_array(A); _validate_bool_array(B)
    return [A[i] or B[i] for i in range(len(A))]

def intersection(A, B):
    _validate_bool_array(A); _validate_bool_array(B)
    return [A[i] and B[i] for i in range(len(A))]

def difference(A, B):
    _validate_bool_array(A); _validate_bool_array(B)
    return [A[i] and not B[i] for i in range(len(A))]

def symmetric_difference(A, B):
    _validate_bool_array(A); _validate_bool_array(B)
    # A ⊕ B = (A - B) ∪ (B - A)
    return union(difference(A, B), difference(B, A))

def run_part1(A, B, case_name):
    print(f"\n===== Part 1 - {case_name} =====\n")
    print_set("A", A)
    print_set("B", B)
    print_set("NOT A (complement)", complement(A))
    print_set("A UNION B", union(A, B))
    print_set("A INTERSECTION B", intersection(A, B))
    print_set("A - B", difference(A, B))
    print_set("A SYMMETRIC DIFFERENCE B", symmetric_difference(A, B))


# -------- Test Case 1 (Partial Overlap) --------
A1 = [True, False, True, False, False, True, False, False, True, False]
B1 = [False, True, True, False, True, False, False, True, False, False]
run_part1(A1, B1, "Test Case 1 (Partial Overlap)")

# -------- Test Case 2 (Identical Sets) --------
A2 = [True, True, False, False, False, False, False, False, False, False]
B2 = [True, True, False, False, False, False, False, False, False, False]
run_part1(A2, B2, "Test Case 2 (Identical Sets)")

# -------- Test Case 3 (Disjoint Sets) --------
A3 = [True, False, False, False, False, False, False, False, False, False]
B3 = [False, True, False, False, False, False, False, False, False, False]
run_part1(A3, B3, "Test Case 3 (Disjoint Sets)")


# =====================================================
# PART 2: Multisets (Bags)
# Representation: dict element -> multiplicity (count)
# =====================================================

def _normalize_multiset(M):
    """Remove zero/negative counts and enforce integer counts."""
    cleaned = {}
    for k, v in M.items():
        if not isinstance(v, int):
            raise TypeError("All multiset counts must be integers.")
        if v > 0:
            cleaned[k] = v
    return cleaned

def print_multiset(label, M):
    """Print in a consistent order using the universe list U when possible."""
    M = _normalize_multiset(M)
    ordered_parts = []
    used = set()

    for e in U:
        if e in M:
            ordered_parts.append(f"{e}:{M[e]}")
            used.add(e)

    extras = sorted(k for k in M.keys() if k not in used)
    for k in extras:
        ordered_parts.append(f"{k}:{M[k]}")

    print(f"{label}: " + "{" + ", ".join(ordered_parts) + "}")

def multiset_union(A, B):
    A = _normalize_multiset(A); B = _normalize_multiset(B)
    result = {}
    keys = set(A.keys()).union(B.keys())
    for k in keys:
        result[k] = max(A.get(k, 0), B.get(k, 0))
    return _normalize_multiset(result)

def multiset_intersection(A, B):
    A = _normalize_multiset(A); B = _normalize_multiset(B)
    result = {}
    keys = set(A.keys()).intersection(B.keys())
    for k in keys:
        result[k] = min(A[k], B[k])
    return _normalize_multiset(result)

def multiset_difference(A, B):
    A = _normalize_multiset(A); B = _normalize_multiset(B)
    result = {}
    for k in A:
        result[k] = max(A[k] - B.get(k, 0), 0)
    return _normalize_multiset(result)

def multiset_sum(A, B):
    A = _normalize_multiset(A); B = _normalize_multiset(B)
    result = {}
    keys = set(A.keys()).union(B.keys())
    for k in keys:
        result[k] = A.get(k, 0) + B.get(k, 0)
    return _normalize_multiset(result)

def run_part2(A, B, case_name):
    print(f"\n===== Part 2 - {case_name} =====\n")
    print_multiset("MultiSet A", A)
    print_multiset("MultiSet B", B)
    print_multiset("Union (A ∪ B, max)", multiset_union(A, B))
    print_multiset("Intersection (A ∩ B, min)", multiset_intersection(A, B))
    print_multiset("Difference (A - B, subtract floor 0)", multiset_difference(A, B))
    print_multiset("Sum (A + B, add)", multiset_sum(A, B))


multiA1 = {"A": 1, "C": 3, "F": 2, "H": 2}
multiB1 = {"B": 1, "C": 2, "F": 1, "H": 4}
run_part2(multiA1, multiB1, "Test Case 1 (Non-trivial)")

multiB2 = {"A": 1, "B": 4, "E": 1, "G": 2}
run_part2(multiA2, multiB2, "Test Case 2 (Representative)")

multiA_edge = {"A": 2, "B": 3}
multiB_edge = {}
run_part2(multiA_edge, multiB_edge, "Edge Case (Empty B)")


# =====================================================
# OPTIONAL: Tiny natural-language query type guess (set vs multiset)
# =====================================================

def guess_query_type(q):
    s = q.strip().lower()
    multiset_markers = ["how many", "count", "number of", "total"]
    set_markers = ["which", "who", "list", "show me", "what are"]

    if any(m in s for m in multiset_markers):
        return ("multiset", "The query asks about counts or frequencies, so multiplicity (duplicates) matters.")
    if any(m in s for m in set_markers):
        return ("set", "The query focuses on membership (which items are included), so duplicates are typically irrelevant.")
    return ("ambiguous", "The wording alone does not clearly indicate whether a set or multiset representation is required.")

def run_query_demo():
    print("\n===== Natural-Language Query Demo (Optional) =====\n")
    examples = [
        "Which customers attended SLCC?",
        "How many customers attended SLCC?",
        "List the students who submitted Project 1",
        "Total number of logins last week",
        "Customers from Utah",
    ]
    for q in examples:
        t, reason = guess_query_type(q)
        print(f"Query: {q}")
        print(f"Guess: {t}  |  Reason: {reason}\n")

run_query_demo()


input("\nPress Enter to exit...")
