'''
阅读理解, leetcode 机翻一样, 罪大恶极
'''
class Solution:
    def maxSumAfterPartitioning(self, arr, k) :
        dic={-1:0,0:arr[0]}
        def get_max(index,length):
            return length*max(arr[index-length+1:index+1])
        def dfs(index,k):
            if index in dic:
                return dic[index]
            max_val = max( get_max(index,i)+dfs(index-i,k) for i in range(1,min(index+1,k)+1) )
            dic[index]=max_val
            return max_val
        return dfs(len(arr)-1,k)
    
if __name__ == '__main__':
    assert Solution().maxSumAfterPartitioning(arr = [1,15,7,9,2,5,10], k = 3) == 84
    assert Solution().maxSumAfterPartitioning(arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4) == 83