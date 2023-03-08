import itertools
import re
from typing import List


class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        class S(set):
            __add__ = lambda s, o: S(s | o)
            __mul__ = lambda s, o: S(i + j for i, j in itertools.product(s, o))
        expression = re.sub('(\w+)', r'S(["\1"])', expression).replace(',', '+').replace('{', '(').replace('}', ')').replace(')(',')*(').replace(')S',')*S')
        return sorted(S(eval(expression)))