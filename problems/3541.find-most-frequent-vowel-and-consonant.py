#
# @lc app=leetcode id=3541 lang=python3
# @lcpr version=30204
#
# [3541] Find Most Frequent Vowel and Consonant
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter


class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq_map = Counter(s)
        vowel_freq = 0
        consonant_freq = 0
        VOWELS = set('aeiou')
        for k, v in freq_map.items():
            if k in VOWELS:
                vowel_freq = max(vowel_freq, v)
            else:
                consonant_freq = max(consonant_freq, v)
        return vowel_freq + consonant_freq
        
# @lc code=end



#
# @lcpr case=start
# "successes"\n
# @lcpr case=end

# @lcpr case=start
# "aeiaeia"\n
# @lcpr case=end

#

