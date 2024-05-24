#
# @lc app=leetcode id=1255 lang=python3
# @lcpr version=
#
# [1255] Maximum Score Words Formed by Letters
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        words_count = [Counter(word) for word in words]
        letters_score = sum([score[ord(c)-ord('a')] for c in letters])
        pointer = {'min_last': letters_score}
        def dfs(i: int, last: Counter):
            if i == len(words_count):
                # print(last)
                last_score = sum(
                    score[ord(char)-ord('a')]*count for char,count in last.most_common()
                )
                pointer['min_last'] = min(pointer['min_last'],last_score) 
                return 
            word_count = words_count[i]
            dfs(i+1, last)
            if not word_count - last:
                dfs(i+1, last-word_count)
        count = Counter(letters)
        dfs(0, count)
        return letters_score - pointer['min_last']
        
# @lc code=end



#
# @lcpr case=start
# ["dog","cat","dad","good"]\n["a","a","c","d","d","d","g","o","o"]\n[1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]\n
# @lcpr case=end

# @lcpr case=start
# ["xxxz","ax","bx","cx"]\n["z","a","b","c","x","x","x"]\n[4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]\n
# @lcpr case=end

# @lcpr case=start
# ["leetcode"]\n["l","e","t","c","o","d"]\n[0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]\n
# @lcpr case=end

#

