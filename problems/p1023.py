from re import match
from typing import List


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        pattern = '^[a-z]*' + '[a-z]*'.join(pattern) + '[a-z]*$'
        return [match(pattern, query) is not None for query in queries]