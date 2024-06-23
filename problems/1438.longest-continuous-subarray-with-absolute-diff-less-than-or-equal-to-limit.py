#
# @lc app=leetcode id=1438 lang=python3
# @lcpr version=
#
# [1438] Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import collections
import heapq
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        subs = (
            nums[left:right+1]
            for left in range(len(nums))
            for right in range(left, len(nums))
        )
        longest_sub_length = 0
        for sub in subs:
            if max(sub)-min(sub) <= limit:
                longest_sub_length = max(longest_sub_length, len(sub))
        return longest_sub_length
        
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        longest = 0
        for left in range(len(nums)):
            pos_heap:List[int] = []
            nag_heap:List[int] = []
            for right in range(left, len(nums)):
                num = nums[right]
                heapq.heappush(pos_heap, num)
                heapq.heappush(nag_heap, -num)

                pos,nag = heapq.heappop(pos_heap),heapq.heappop(nag_heap)
                diff = abs(pos+nag)
                heapq.heappush(pos_heap,pos)
                heapq.heappush(nag_heap,nag)
                if diff <= limit:
                    longest = max(len(pos_heap), longest)
                else:
                    break
            else:
                return longest
        return longest

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        decQ = collections.deque() 
        incQ = collections.deque() 
        ans = 0
        left = 0
        for right, num in enumerate(nums):
            while decQ and num > decQ[-1]:
                decQ.pop()
            decQ.append(num)
            while incQ and num < incQ[-1]:
                incQ.pop()
            incQ.append(num)
            while decQ[0] - incQ[0] > limit:
                if decQ[0] == nums[left]:
                    decQ.popleft()
                if incQ[0] == nums[left]:
                    incQ.popleft()
                left += 1
            ans = max(ans, right - left + 1)
        return ans
# @lc code=end

print(Solution().longestSubarray([4,2,2,2,4,4,2,2],0))

#
# @lcpr case=start
# [8,2,4,7]\n4\n
# @lcpr case=end

# @lcpr case=start
# [10,1,2,4,7,2]\n5\n
# @lcpr case=end

# @lcpr case=start
# [4,2,2,2,4,4,2,2]\n0\n
# @lcpr case=end

#

