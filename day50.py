# Create a program that finds the intersection and union of two sets.


def find_intersection_union(set1, set2) -> tuple:
    """Find the intersection and union of two sets.

    Args:
        set1 (sets): The first set.
        set2 (sets): The second set.

    Returns:
        tuple: A tuple containing the intersection and union of the two sets.
    """
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return (intersection, union)


# Example usage
SET1 = {1, 2, 3, 4, 5}
SET2 = {4, 5, 6, 7, 8}
print(find_intersection_union(SET1, SET2))
# Output: ({4, 5}, {1, 2, 3, 4, 5, 6, 7, 8})

SET3 = {9, 10, 11, 12, 13}
SET4 = {12, 13, 14, 15, 16}
print(find_intersection_union(SET3, SET4))
# Output: ({12, 13}, {9, 10, 11, 12, 13, 14, 15, 16})
