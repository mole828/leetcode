from typing import List


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        ans = 0
        c = [0 for _ in range(26)]
        for cc in letters:
            c[ord(cc) - ord('a')] += 1
        n = len(words)
        for i in range(1 << n):
            tmp = [0 for _ in range(26)]
            sc = 0
            for j in range(n): # 遍历状态
                print(f"{i}&{1<<j} -> {i&(1<<j)} -> {True if i&(1<<j) else False}" )
                if i & (1 << j): # 1: [1], 2: [10,11], 3:[01,10] ...
                    for k in words[j]:
                        tmp[ord(k) - ord('a')] += 1
            f = 1
            for j in range(26):
                if tmp[j] > c[j]:
                    f = 0
                    break
                sc += tmp[j] * score[j]
            if f:
                ans = max(ans,sc)
        return ans 

if __name__ == '__main__':
    Solution().maxScoreWords(
        words = ["dog","cat","dad","good"], 
        letters = ["a","a","c","d","d","d","g","o","o"], 
        score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
    )