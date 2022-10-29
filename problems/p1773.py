from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        key = ['type', 'color', 'name'].index(ruleKey)
        return sum(1 for item in items if item[key]==ruleValue)
        