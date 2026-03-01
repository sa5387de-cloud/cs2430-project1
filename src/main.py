# CS2430 Programming Project 1
# Sets, Multisets, and Natural-Language Data Queries
# Hanseo Yun

# =====================================================
# PART 1: Ordinary Sets (Boolean Arrays)
# =====================================================

U = ["A","B","C","D","E","F","G","H","I","J"]

def print_set(name, bool_array):
    elements = [U[i] for i in range(len(U)) if bool_array[i]]
    print(f"{name} (bool): {bool_array}")
    print(f"{name} (elements): {elements}")
    print()

def complement(A):
    return [not x for x in A]

def union(A, B):
    return [A[i] or B[i] for i in range(len(A))]

def intersection(A, B):
    return [A[i] and B[i] for i in range(len(A))]

def difference(A, B):
    return [A[i] and not B[i] for i in range(len(A))]

def symmetric_difference(A, B):
    return union(difference(A,B), difference(B,A))

def run_part1(A, B, case_name):
    print(f"\n===== Part 1 - {case_name} =====\n")
    print_set("A", A)
    print_set("B", B)
    print_set("NOT A", complement(A))
    print_set("A UNION B", union(A,B))
    print_set("A INTERSECTION B", intersection(A,B))
    print_set("A - B", difference(A,B))
    print_set("A SYMMETRIC DIFFERENCE B", symmetric_difference(A,B))


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
# =====================================================

def multiset_union(A,B):
    result = {}
    keys = set(A.keys()).union(B.keys())
    for k in keys:
        result[k] = max(A.get(k,0), B.get(k,0))
    return result

def multiset_intersection(A,B):
    result = {}
    keys = set(A.keys()).intersection(B.keys())
    for k in keys:
        result[k] = min(A[k], B[k])
    return result

def multiset_difference(A,B):
    result = {}
    for k in A:
        result[k] = max(A[k] - B.get(k,0), 0)
    return result

def multiset_sum(A,B):
    result = {}
    keys = set(A.keys()).union(B.keys())
    for k in keys:
        result[k] = A.get(k,0) + B.get(k,0)
    return result

def run_part2(A, B, case_name):
    print(f"\n===== Part 2 - {case_name} =====\n")
    print("MultiSet A:", A)
    print("MultiSet B:", B)
    print("Union:", multiset_union(A,B))
    print("Intersection:", multiset_intersection(A,B))
    print("Difference (A-B):", multiset_difference(A,B))
    print("Sum (A+B):", multiset_sum(A,B))


# -------- Multiset Test Case 1 --------
multiA1 = {"A":1, "C":3, "F":2, "H":2}
multiB1 = {"B":1, "C":2, "F":1, "H":4}
run_part2(multiA1, multiB1, "Test Case 1")


# -------- Multiset Edge Case (Empty B) --------
multiA2 = {"A":2, "B":3}
multiB2 = {}
run_part2(multiA2, multiB2, "Edge Case (Empty B)")


input("\nPress Enter to exit...")
