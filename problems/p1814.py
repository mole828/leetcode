from collections import Counter
from typing import List

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        ans=0; cnt=Counter()
        for c in nums:
            tmp=c-int(str(c)[::-1])
            ans+=cnt[tmp]
            cnt[tmp]+=1
        return ans%(10**9+7)
        
if __name__ == '__main__':
    Solution().countNicePairs([42,11,1,97])