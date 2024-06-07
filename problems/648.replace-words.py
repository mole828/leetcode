#
# @lc app=leetcode id=648 lang=python3
# @lcpr version=
#
# [648] Replace Words
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort()
        result = []
        for sent in sentence.split():
            for word in dictionary:
                if sent.startswith(word):
                    result.append(word)
                    break
            else:
                result.append(sent)
        return ' '.join(result)
# @lc code=end



#
# @lcpr case=start
# ["cat","bat","rat"]\n"the cattle was rattled by the battery"\n
# @lcpr case=end

# @lcpr case=start
# ["a","b","c"]\n"aadsfasf absbs bbab cadsfafs"\n
# @lcpr case=end

#

