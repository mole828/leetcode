#
# @lc app=leetcode id=726 lang=python3
# @lcpr version=
#
# [726] Number of Atoms
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def classify(form: list[str]) -> list[str,int]:
            stack = []
            for c in form:
                try:
                    ic = int(c)
                    if type(stack[-1]) is int:
                        ic = stack.pop()*10 + ic
                    stack.append(ic)
                    continue
                except:
                    pass
                if c == c.upper():
                    stack.append(c)
                else:
                    last = stack.pop()
                    stack.append(last+c)
            return stack
        
        def count(words: list[str, int, Counter]) -> Counter:
            print('count in',words)
            stack = []
            for word in words:
                if word == ')':
                    new_stack = []
                    while stack:
                        _word = stack.pop()
                        if _word == '(':
                            break
                        new_stack.insert(0, _word)
                    _count = count(new_stack)
                    stack.append(_count)
                    continue
                stack.append(word)
            _count = Counter()
            while stack:
                last = stack.pop()
                if type(last) is Counter:
                    _count.update(last)
                elif type(last) is int:
                    sec = stack.pop()
                    stack += [sec]*last
                else:
                    _count[last] += 1
            return _count
        full_stack = classify([c for c in formula])
        counter = count(full_stack)
        return ''.join([f"{k}{v}" if v>1 else k for k,v in sorted(counter.items())])

        

# @lc code=end

print(Solution().countOfAtoms("H2O"))
print(Solution().countOfAtoms("Mg(OH)2"))


#
# @lcpr case=start
# "H2O"\n
# @lcpr case=end

# @lcpr case=start
# "Mg(OH)2"\n
# @lcpr case=end

# @lcpr case=start
# "K4(ON(SO3)2)2"\n
# @lcpr case=end

#

