class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        begin, end = index, index+1
        
        summary = n
        ans = 1
        if maxSum > n*n:
            ne = maxSum - n*n
            i = ne//n
            summary = i * n
            ans = i 
            
        while summary<maxSum:
            ans += 1
            summary += end-begin
            begin = max(begin-1, 0)
            end = min(end+1, n)
        return ans if summary==maxSum else ans-1