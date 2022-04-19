from collections import defaultdict


def is_isomorphic(str_1: str, str_2: str) -> bool:
    if len(str_1) != len(str_2):
        return False

    str_map = defaultdict(int)
    used = set()

    for i in range(len(str_1)):
        if str_1[i] in str_map:
            if str_map[str_1[i]] != str_2[i]:
                return False
        else:
            if str_2[i] in used:
                return False
            str_map[str_1[i]] = str_2[i]
            used.add(str_2[i])
    return True


if __name__ == "__main__":
    str1 = 'aba'
    str2 = 'xax'
    print(is_isomorphic(str1, str2))
    str_a = 'wow'
    str_b = 'aaa'
    print(is_isomorphic(str_a, str_b))