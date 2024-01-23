# Write a program to shuffle the elements of a list randomly.

from random import shuffle


def shuffle_list(list_to_shuffle) -> list:
    """
    Shuffle the elements of a list randomly.

    Args:
        list_to_shuffle (list): list to shuffle

    Returns:
        list: shuffled list
    """

    shuffle(list_to_shuffle)
    return list_to_shuffle


lst1 = ["Python", "Swift", "C++"]
lst2 = [1, 2, 3, 4, 5]

print(shuffle_list.__doc__)
print("The first list is: ", lst1)
print("The second list is: ", lst2)

print("The first list shuffled is: ", shuffle_list(lst1))
print("The second list shuffled is: ", shuffle_list(lst2))
