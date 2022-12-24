class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        res=''
        i,j=0,0
        m,n=len(word1),len(word2)
        while i<m and j<n:
            if word1[i:]>word2[j:]:
                res+=word1[i]
                i+=1
            else:
                res+=word2[j]
                j+=1
        if i<m:
            res+=word1[i:]
        else:
            res+=word2[j:]
        return res