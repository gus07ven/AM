from typing import List


def find_boundary(arr: List[bool]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    low = 0
    high = len(arr)

    while low <= high:
        mid = high + low // 2
        if arr[mid] == 'true':
            if arr[mid - 1] == 'false':
                return mid
        elif arr[mid] == 'false' and mid > 0 or mid < len(arr):
            low = mid + 1
        else:
            high = mid - 1





