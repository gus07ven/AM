from typing import List
import collections


def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagram_map = {}
    for entry in strs:
        anagram_id = "".join(sorted(entry))
        if anagram_id in anagram_map:
            anagram_map[anagram_id].append(entry)
        else:
            anagram_map[anagram_id] = [entry]

    res = list(anagram_map.values())

    for row in res:
        row.sort()
    res.sort(key=lambda row: row[0])
    return res


def group_anagrams_optimized(strs: List[str]) -> List[List[str]]:
    ans = collections.defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        ans[tuple(count)].append(s)
    res = list(ans.values())

    for row in res:
        row.sort()
    res.sort(key=lambda row: row[0])
    return res


if __name__ == '__main__':
    input = "eat tea tan ate nat bat"
    strs = input.split()
    result = group_anagrams(strs)
    print(result)

    result2 = group_anagrams_optimized(strs)
    print(result2)

    
