#
# @lc app=leetcode id=1233 lang=python3
# @lcpr version=
#
# [1233] Remove Sub-Folders from the Filesystem
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        ans = [folder[0]]
        for f in folder[1:]:
            m, n = len(ans[-1]), len(f)
            if m >= n or not (ans[-1] == f[:m] and f[m] == '/'):
                ans.append(f)
        return ans
# @lc code=end



#
# @lcpr case=start
# ["/a","/a/b","/c/d","/c/d/e","/c/f"]\n
# @lcpr case=end

# @lcpr case=start
# ["/a","/a/b/c","/a/b/d"]\n
# @lcpr case=end

# @lcpr case=start
# ["/a/b/c","/a/b/ca","/a/b/d"]\n
# @lcpr case=end

#

