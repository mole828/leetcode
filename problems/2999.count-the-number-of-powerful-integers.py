#
# @lc app=leetcode id=2999 lang=python3
#
# [2999] Count the Number of Powerful Integers
#

# @lc code=start
import math


class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, suffix: str) -> int:
        limit_set = set(str(n) for n in range(limit+1))
        count = 0
        for num in range(start, finish + 1): 
            num_str = str(num)
            if num_str.endswith(suffix) and all(c in limit_set for c in num_str):
                count += 1
        return count


class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, suffix: str) -> int:
        limit_str_set = set(str(n) for n in range(limit+1))
        result_set = set()
        finish_length = len(str(finish))
        
        def dfs(num_str: str):
            num = int(num_str)
            if not all(c in limit_str_set for c in num_str): return
            if len(num_str) > finish_length: return
            if start <= num <= finish: 
                result_set.add(num)
            
            for c in [str(_s) for _s in range(0, 10)]:  
                new_num_str = c + num_str
                dfs(str(new_num_str))
        dfs(suffix)

        return len(result_set)

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, suffix: str) -> int:
        suffix_num = int(suffix)
        def find_big(x):
            if suffix_num > x:  # s数值大于最大值，则返回0
                return 0
            if len(str(x)) == len(suffix):  # 如果s长度等于最大值长度，则返回1
                return 1
            else:  # 如果s长度小于最大值长度的情况
                if int(str(x)[0]) > limit: # 当s的第一位的数值大于limit，则除s位之外的各个位数都可取0~limit，排列组合即可
                    ss = limit + 1
                    for i in range(1, len(str(x))-len(suffix)):
                        ss *= (limit + 1)
                    return ss
                else: 
                    ss = int(str(x)[0])  # 当s的第一位的数值小于limit，且当str(x)第一位取值为0~int(str(x)[0])-1时
                    for _ in range(1, len(str(x))-len(suffix)):  #并且除s位之外的各个位数都可取0~limit，排列组合即可
                        ss *= (limit + 1)
                    if len(str(x))-len(suffix) >= 1:  # 当s的第一位的数值小于limit，且当str(x)第一位取值为int(str(x)[0])时，递归
                        ss += find_big(int(str(x)[1:]))
                    return ss
        
        return find_big(finish) - find_big(start - 1)
        



# @lc code=end

print(Solution().numberOfPowerfulInt(1, 6000, 4, '124'))
# print(Solution().numberOfPowerfulInt(15, 215, 6, '10'))
# print(Solution().numberOfPowerfulInt(20, 1159, 5, '20'))