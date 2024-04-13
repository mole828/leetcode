#
# @lc app=leetcode id=85 lang=python3
# @lcpr version=
#
# [85] Maximal Rectangle
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    # Time Limit Exceeded, 68/74 cases passed
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows = len(matrix) 
        cols = len(matrix[0]) 
        max_area = 0
        for top in range(rows):
            for left in range(cols):
                v = matrix[top][left] 
                if v:
                    for bottom in range(top, rows):
                        for right in range(left, cols):
                            if all(
                                all(int(matrix[y][x]) for x in range(left, right+1))
                                for y in range(top, bottom+1)
                            ):
                                # top_row = [matrix[top][x] for x in range(left,right+1)]
                                # print({
                                #     'top':top,
                                #     'bottom':bottom,
                                #     'left':left,
                                #     'right':right,
                                #     'top_row': top_row,
                                #     'all(top_row)': all(top_row)
                                # })
                                w = right - left + 1 
                                h = bottom - top + 1
                                area = w * h 
                                max_area = max(max_area, area)
        return max_area
    
# https://algo.monster/liteproblems/85
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # This function finds the maximal rectangle of '1's in a binary matrix.
      
        # Initialize the heights array with zeros based on the width of the matrix
        heights = [0] * len(matrix[0])
        # Initialize the answer to 0, which will hold the area of the largest rectangle
        max_area = 0
      
        # Iterate through each row in the binary matrix
        for row in matrix:
            # Update heights reflecting continuous '1's in a column
            for col_idx, val in enumerate(row):  # col_idx is the index, val is the value at that position
                if val == "1":
                    # Increase the current column's height if the row value is a '1'
                    heights[col_idx] += 1
                else:
                    # Reset the height to 0 if the row value is '0'
                    heights[col_idx] = 0
          
            # Update the max_area with the largest rectangle found in the current histogram of heights
            max_area = max(max_area, self.largestRectangleArea(heights))
      
        # Return the maximal rectangle area found
        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        # This function calculates the largest rectangle in a histogram.
      
        # Length of the heights list
        num_heights = len(heights)
      
        # Stack to keep track of indices for heights
        stack = []
      
        # Arrays to store indices of previous and next smaller heights
        prev_smaller = [-1] * num_heights
        next_smaller = [num_heights] * num_heights
      
        # Forward pass to find previous smaller heights
        for i, height in enumerate(heights):
            # If the current height is lesser than the height at the stack's top index,
            # pop the stack until a smaller height is found
            while stack and heights[stack[-1]] >= height:
                stack.pop()
            if stack:
                prev_smaller[i] = stack[-1]
            stack.append(i)
      
        # Reset stack for next pass
        stack = []
      
        # Backward pass to find next smaller heights
        for i in range(num_heights - 1, -1, -1):
            cur_height = heights[i]
            while stack and heights[stack[-1]] >= cur_height:
                stack.pop()
            if stack:
                next_smaller[i] = stack[-1]
            stack.append(i)
      
        # Calculate the largest rectangle area by finding the maximum area
        # for each height, considering the distance to the previous and next smaller heights.
        max_area = max(
            height * (next_smaller[i] - prev_smaller[i] - 1) for i, height in enumerate(heights)
        )
      
        # Return the maximum area found
        return max_area
 

# @lc code=end

print(Solution().maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))


#
# @lcpr case=start
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["1"]]\n
# @lcpr case=end

#

