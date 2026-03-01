# CS2430 Project 1
# Hanseo Yun
# Part 1: Ordinary Sets using Boolean Arrays
# Part 2: Multisets using Dictionary (Map)

# -----------------------------
# Part 1 - Ordinary Sets
# -----------------------------

# Universal set (n >= 10)
U = ["A","B","C","D","E","F","G","H","I","J"]

# Boolean representation of sets A and B
A = [True, False, True, False, False, True, False, False, True, False]
B = [False, True, True, False, True, False, False, True, False, False]

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


print("===== Part 1: Ordinary Sets =====\n")

print_set("A", A)
print_set("B", B)

print_set("NOT A", complement(A))
print_set("A UNION B", union(A,B))
print_set("A INTERSECTION B", intersection(A,B))
print_set("A - B", difference(A,B))
print_set("A SYMMETRIC DIFFERENCE B", symmetric_difference(A,B))


# -----------------------------
# Part 2 - Multisets
# -----------------------------

print("\n===== Part 2: Multisets =====\n")

# Multisets (with multiplicity >1 in both A and B)
multiA = {"A":1, "C":3, "F":2, "H":2}
multiB = {"B":1, "C":2, "F":1, "H":4}

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

print("MultiSet A:", multiA)
print("MultiSet B:", multiB)
print()

print("Union:", multiset_union(multiA, multiB))
print("Intersection:", multiset_intersection(multiA, multiB))
print("Difference (A-B):", multiset_difference(multiA, multiB))
print("Sum (A+B):", multiset_sum(multiA, multiB))
