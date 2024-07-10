#
# @lc app=leetcode id=1598 lang=python3
# @lcpr version=
#
# [1598] Crawler Log Folder
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        total = 0
        for log in logs:
            if log == './':
                pass
            elif log == '../':
                total = max(0, total-1)
            else:
                total += 1
        return total
        
# @lc code=end



#
# @lcpr case=start
# ["d1/","d2/","../","d21/","./"]\n
# @lcpr case=end

# @lcpr case=start
# ["d1/","d2/","./","d3/","../","d31/"]\n
# @lcpr case=end

# @lcpr case=start
# ["d1/","../","../","../"]\n
# @lcpr case=end

#

