# https://leetcode.com/problems/group-anagrams/
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    dict = {}
    for item in strs:
        # ? list는 dictionary의 key가 될 수 없다. (immutable type만 key로 사용 가능)
        key = tuple(sorted(item))
        if key in dict:
            dict[key].append(item)
        else:
            dict[key] = []
            dict[key].append(item)

    return [dict[items] for items in dict]


groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

