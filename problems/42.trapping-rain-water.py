#
# @lc app=leetcode id=42 lang=python3
# @lcpr version=
#
# [42] Trapping Rain Water
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    # Time Limit Exceeded, 318/322 cases passed 
    def trap(self, height: List[int]) -> int: 
        count = 0 
        length = len(height)
        for left in range(length): 
            left_height = height[left] 
            for right in range(left, length): 
                right_height = height[right] 
                min_height = min(left_height,right_height) 
                # print(left, right, min_height) 
                for i in range(left,right): 
                    h = height[i] 
                    if h < min_height: 
                        height[i] = min_height 
                        count += min_height - h 
        return count 
    
    # Accepted, runtime 5%, memeory 7.16%
    def trap(self, height: List[int]) -> int: 
        count = 0 
        stack:list[tuple[int,int]] = [(-1, 0)]  
        for i, h in enumerate(height): 
            left, left_h = stack[-1] 
            min_h = min(left_h, h) 
            for j in range(left, i):
                j_h = height[j] 
                if j_h < min_h: 
                    height[j] = min_h 
                    count += min_h - j_h
            if h > left_h: 
                stack.append((i,h)) 
        return count 
    
    def trap(self, height: List[int]) -> int: 
        count = 0 
        stack = [] 
        for right, right_h in enumerate(height): 
            while stack and height[stack[-1]] < right_h: 
                min_i = stack.pop() 
                if not stack: break
                left = stack[-1] 
                dh = min(right_h, height[left]) - height[min_i] 
                width = right - left - 1 
                count += dh * width 
            stack.append(right) 
        return count 

# @lc code=end

print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))

#
# @lcpr case=start
# [0,1,0,2,1,0,1,3,2,1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,2,0,3,2,5]\n
# @lcpr case=end

#

