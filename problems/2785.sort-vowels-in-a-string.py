#
# @lc app=leetcode id=2785 lang=python3
#
# [2785] Sort Vowels in a String
#
# 文字理解


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def sortVowels(self, input_str: str) -> str:
        vowels_list = []
        vowel_positions = []
        
        for index, char in enumerate(input_str):
            if char.lower() in {'a', 'e', 'i', 'o', 'u'}:
                vowels_list.append(char)
                vowel_positions.append(index)

        vowels_list.sort()
        result_list = list(input_str)
        
        for position, vowel in zip(vowel_positions, vowels_list):
            result_list[position] = vowel
        
        return ''.join(result_list)
# @lc code=end

print(Solution().sortVowels("lEetcOde"))

