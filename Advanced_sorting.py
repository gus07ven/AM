from typing import List


# O(n log n), stable, not in-place
# Pros: fast, stable
# Cons: Not in-place
def merge_sort(unsorted_list: List[int]) -> List[int]:
    n = len(unsorted_list)
    if n <= 1:
        return unsorted_list

    # Split
    midpoint = n // 2
    left_list, right_list = merge_sort(unsorted_list[:midpoint]), merge_sort(unsorted_list[midpoint:])

    # Merge
    result = []
    left_ptr, right_ptr = 0, 0
    while left_ptr < midpoint or right_ptr < n - midpoint:
        if left_ptr == midpoint:
            result.append(right_list[right_ptr])
            right_ptr += 1
        elif right_ptr == n - midpoint:
            result.append(left_list[left_ptr])
            left_ptr += 1
        elif left_list[left_ptr] <= right_list[right_ptr]:
            result.append(left_list[left_ptr])
            left_ptr += 1
        else:
            result.append(right_list[right_ptr])
            right_ptr += 1
    return result


if __name__ == '__main__':

    # Merge sort
    unsorted_list = [5, 3, 1, 2, 4]
    res_ms = merge_sort(unsorted_list)
    print(' '.join(map(str, res_ms)))
