def linear_search(arr, target):
    """
    Searches for a target value in a list using linear search.

    Args:
        arr (list): A list of elements to search through
        target: The value to search for

    Returns:
        int: Index of target if found, otherwise -1
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1


if __name__ == "__main__":
    numbers = [4, 2, 7, 1, 9]
    target = 7

    result = linear_search(numbers, target)

    if result != -1:
        print(f"Target found at index {result}")
    else:
        print("Target not found")
