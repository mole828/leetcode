from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        firstIndex = [sum(nums[i:i+firstLen]) for i in range(len(nums)-firstLen+1)]
        secondIndex = [sum(nums[i:i+secondLen]) for i in range(len(nums)-secondLen+1)]
        # print(firstIndex,secondIndex)
        ans = -1
        for a in range(len(firstIndex)):
            for b in range(firstLen+a, len(secondIndex)):
                # print(a,b, firstIndex[a], secondIndex[b])
                ans = max(ans, firstIndex[a]+secondIndex[b])
        for a in range(len(secondIndex)):
            for b in range(secondLen+a, len(firstIndex)):
                # print(a,b, secondIndex[a], firstIndex[b])
                ans = max(ans, secondIndex[a]+firstIndex[b])
        # print(ans)
        return ans

if __name__ == '__main__':
    s = Solution()
    assert s.maxSumTwoNoOverlap(nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2) == 20
    assert s.maxSumTwoNoOverlap([2,1,5,6,0,9,5,0,3,8],4,3) == 31