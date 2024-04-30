#
# @lc app=leetcode id=1915 lang=python3
# @lcpr version=
#
# [1915] Number of Wonderful Substrings
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start


from collections import Counter


class Solution:
    # Time Limit Exceeded, 48/88 cases passed (N/A)
    def wonderfulSubstrings(self, word: str) -> int:
        def is_wonderful(word: str):
            counter = Counter(word)
            has_wonder = False
            for k in counter:
                # print(k, counter[k])
                if has_wonder and counter[k]%2:
                    return False
                if counter[k]%2 :
                    has_wonder = True
            return True
        ans = 0
        for left in range(len(word)):
            for right in range(left, len(word)):
                sub = word[left:right+1]
                if is_wonderful(sub):
                    # print(sub)
                    ans += 1
        return ans
        
    # Time Limit Exceeded, 57/88 cases passed (N/A)
    def wonderfulSubstrings(self, word: str) -> int:
        ans = 0
        for left in range(len(word)):
            counter: Counter[str] = Counter()
            wonders: set[str] = set()
            for right in range(left, len(word)):
                right_char = word[right]
                counter[right_char] += 1
                if counter[right_char] % 2:
                    wonders.add(right_char)
                else:
                    wonders.remove(right_char)
                if len(wonders) < 2:
                    ans += 1
        return ans

    def wonderfulSubstrings(self, word: str) -> int:
        ans = 0
        sum_mask = 0
        mask_counter = Counter()
        mask_counter[sum_mask] += 1
        for char in word:
            char_index = ord(char) - ord('a')
            mask = 1 << char_index
            sum_mask ^= mask
            ans += mask_counter[sum_mask]
            ans += sum(mask_counter[sum_mask^(1<<i)] for i in range(10))
            mask_counter[sum_mask] += 1
        return ans
# @lc code=end

print(Solution().wonderfulSubstrings("aba"))

#
# @lcpr case=start
# "aba"\n
# @lcpr case=end

# @lcpr case=start
# "aabb"\n
# @lcpr case=end

# @lcpr case=start
# "he"\n
# @lcpr case=end

#

