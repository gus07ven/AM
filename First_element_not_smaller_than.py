from typing import List


def first_not_smaller(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    not_smaller = 0

    while left <= right:
        mid = (right + left) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] >= target:
            not_smaller = mid
            right = mid - 1

    return not_smaller


if __name__ == '__main__':
    arr = [1, 3, 3, 5, 8, 8, 10]
    target = 2
    print(first_not_smaller(arr, target))