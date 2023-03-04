from typing import List


class Solution:
    def countTriplets(self, nums: List[int]) -> int:
    
        def FWT(N, arr):
            mid = 1
            while mid < N:
                j, block = 0, mid << 1
                while j < N:
                    for i in range(j, j + mid):
                        arr[i] = arr[i] + arr[i + mid]
                    j += block
                mid <<= 1
            
        def IFWT(N, arr):
            mid = 1
            while mid < N:
                j, block = 0, mid << 1
                while j < N:
                    for i in range(j, j + mid):
                        arr[i] = arr[i] - arr[i + mid]
                    j += block
                mid <<= 1
        
        # Find N for FWT
        maxx_num = max(nums)
        N = 4
        while N <= maxx_num:
            N <<= 1
        arr = [0] * N
        for num in nums:
            arr[num] += 1
        FWT(N, arr)
        arr_3rd = [a ** 3 for a in arr]
        IFWT(N, arr_3rd)
        return arr_3rd[0]