#
# @lc app=leetcode id=3016 lang=python3
# @lcpr version=
#
# [3016] Minimum Number of Pushes to Type Word II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumPushes(self, word: str) -> int:
        return sum(f*(i//8+1) for i, f in enumerate(sorted(Counter(word).values(), reverse=True)))
        
# @lc code=end



#
# @lcpr case=start
# "abcde"\n
# @lcpr case=end

# @lcpr case=start
# "xyzxyzxyzxyz"\n
# @lcpr case=end

# @lcpr case=start
# "aabbccddeeffgghhiiiiii"\n
# @lcpr case=end

#

