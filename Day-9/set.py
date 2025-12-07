# Set

set1 = {1,2,3,4}
set2 = {3,4,5,6}

# Add and remove elements in set
set1.add(5)
set1.remove(1)
print(set1)

set2.add(7)
set2.remove(3)
print(set2)


# Union, intersection and difference in set
union_set = set1.union(set2)
print(union_set)

intersection_set = set1.intersection(set2)
print(intersection_set)

difference_set = set1.difference(set2)
print(difference_set)

# Subset and superset

is_subset = set1.issubset(set2)
print(is_subset)

is_superset = set1.issuperset(set2)
print(is_superset)





