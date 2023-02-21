from typing import List


class Solution:
    def minTaps(self, n: int, lengths: List[int]) -> int:
        l2r = [0]*(n+1)
        for (center,length) in enumerate(lengths):
            left = max(center-length, 0)
            right = min(center+length, n)
            l2r[left] = max(l2r[left], right)

        ans = last = pre = 0
        for (left,right) in enumerate(l2r):
            if left == n:break
            last = max(last,right)
            if left == last:return -1
            if left == pre:
                ans += 1
                pre = last

        return ans
    

if __name__ == '__main__':
    Solution().minTaps(5,[3,4,1,1,0,0])