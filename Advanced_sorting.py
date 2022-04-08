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


# Average: O(n log n), worse case: O(n^2)
# Pros: in-place
# Cons: not stable, worse case could take O(n^2)
def sort_list_interval(unsorted_list: List[int], start: int, end: int):
    if end - start <= 1:
        return

    pivot = unsorted_list[end - 1]
    start_ptr = start
    end_ptr = end - 1

    while start_ptr < end_ptr:
        while unsorted_list[start_ptr] < pivot and start_ptr < end_ptr:
            start_ptr += 1
        while unsorted_list[end_ptr] >= pivot and start_ptr < end_ptr:
            end_ptr -= 1
        if start_ptr == end_ptr:
            break
        unsorted_list[start_ptr], unsorted_list[end_ptr] = unsorted_list[end_ptr], unsorted_list[start_ptr]
    unsorted_list[start_ptr], unsorted_list[end - 1] = unsorted_list[end - 1], unsorted_list[start_ptr]
    sort_list_interval(unsorted_list, start, start_ptr)
    sort_list_interval(unsorted_list, start_ptr + 1, end)


def quick_sort(unsorted_list: List[int]) -> List[int]:
    sort_list_interval(unsorted_list, 0, len(unsorted_list))


if __name__ == '__main__':

    # Merge sort
    unsorted_list = [5, 3, 1, 2, 4]
    res_ms = merge_sort(unsorted_list)
    print(' '.join(map(str, res_ms)))

    # Quick sort
    unsorted_list = [5, 3, 1, 2, 4]
    quick_sort(unsorted_list)
    print(' '.join(map(str, unsorted_list)))

