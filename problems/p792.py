from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans = 0
        for word in words:
            sc = s[:]
            isMatchingSubseq = True
            for char in word:
                try: 
                    i = sc.index(char)
                except:
                    isMatchingSubseq = False
                    break
                sc = sc[i+1:]
                print(sc)
            if isMatchingSubseq:ans+=1
        return ans
