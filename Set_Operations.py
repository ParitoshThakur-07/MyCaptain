E = {1, 2, 3, 4, 5}
N = {4, 5, 6, 7, 8}

print("set 1 :",E)
print("set 2 :",N)

union_set = E.union(N)
print(f"Union of set 1 and N: {union_set}")

# Perform intersection operation
intersection_set = E.intersection(N)
print(f"Intersection of E and N: {intersection_set}")

# Perform difference operation (E - N)
difference_E = E.difference(N)
print(f"Difference of E and N (E - N): {difference_E}")

# Perform difference operation (N - E)
difference_N = N.difference(E)
print(f"Difference of E and N (N - E): {difference_N}")

# Perform symmetric difference operation
symmetric_difference_set = E.symmetric_difference(N)
print(f"Symmetric difference of E and N: {symmetric_difference_set}")
