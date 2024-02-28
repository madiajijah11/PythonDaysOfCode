# Create a program that implements the bubble sort algorithm.


def bubble_sort(arr):
    """
        Bubble sort algorithm.

    Args:
        arr (list): List of elements to be sorted.

    Returns:
        list: List of elements sorted in ascending order.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Test cases
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))  # [11, 12, 22, 25, 34, 64, 90]
print(bubble_sort([5, 1, 4, 2, 8]))  # [1, 2, 4, 5, 8]
