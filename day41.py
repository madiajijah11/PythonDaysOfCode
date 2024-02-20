# Write a program that uses recursion to generate all permutations of a list.


def permutations(lst):
    """
    Generate all permutations of a list using recursion.

    Args:
        lst (list): The list to generate permutations for.

    Returns:
        list: A list of all permutations of the input list.
    """
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i + 1 :]
        for p in permutations(remLst):
            l.append([m] + p)
    return l


# Test the function
print(permutations([1, 2, 3]))
