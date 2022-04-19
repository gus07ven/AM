from typing import List


def binary_search(arr: List[int], target: int) -> int:
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


if __name__ == '__main__':
    arr = [i for i in range(1, 7)]
    print(f'Find the index of number 6: {binary_search(arr, 6)}')
