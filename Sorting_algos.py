from typing import List

# O(n^2), stable, in-place.
# Pros: Good for sorting list almost sorted (almost at O(1)). Used for smaller lists in Python's Timsort.
# Cons: Slow.
def insertion_sort(unsorted_list: List[int]) -> List[int]:
    for i, entry in enumerate(unsorted_list):
        current = i
        while current > 0 and unsorted_list[current] < unsorted_list[current - 1]:
            unsorted_list[current], unsorted_list[current - 1] = unsorted_list[current - 1], unsorted_list[current]
            current -= 1
    return unsorted_list

def selection_sort(unsorted_list: List[int]) -> List[int]:
    n = len(unsorted_list)
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if unsorted_list[j] < unsorted_list[min_index]:
                min_index = j
        unsorted_list[i], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[i]
    return unsorted_list


if __name__ == '__main__':

    # Insertion sort
    unsorted_list = [5, 3, 1, 2, 4]
    res = insertion_sort(unsorted_list)
    print(' '.join(map(str, res)))

    unsorted_list = [5, 3, 1, 2, 4]
    res = selection_sort(unsorted_list)
    print(' '.join(map(str, res)))