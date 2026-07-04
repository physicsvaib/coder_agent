
def insertion_sort(arr):
    """
    Sorts an array using the insertion sort algorithm.

    Parameters:
    arr (list): A list of elements to be sorted.

    Returns:
    list: The sorted list.
    """
    # Traverse from 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

# Example usage
if __name__ == "__main__":
    unsorted_list = [12, 11, 13, 5, 6]
    print("Unsorted list:", unsorted_list)
    sorted_list = insertion_sort(unsorted_list)
    print("Sorted list:", sorted_list)
