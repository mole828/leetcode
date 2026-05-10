package problems.p2770

import kotlin.math.absoluteValue

/*
 * @lc app=leetcode id=2770 lang=kotlin
 *
 * [2770] Maximum Number of Jumps to Reach the Last Index
 */
// @lc code=start
class Solution {
    @Deprecated("TLE")
    fun maximumJumps0(nums: IntArray, target: Int): Int {
        val cache = mutableMapOf<Int, Int>()
        fun dfs(j: Int): Int = cache.getOrPut(j) { 
            if(j==0) return 0
            var re = Int.MIN_VALUE
            for(i in 0..<j) {
                if((nums[i] - nums[j]).absoluteValue <= target) {
                    re = maxOf(re, dfs(i) + 1)
                }
            }
            return re
        }
        val ans = dfs(nums.size - 1)
        return if (ans<0) -1 else ans
    }
    fun maximumJumps(nums: IntArray, target: Int): Int {
        val n = nums.size
        val dp = IntArray(n) { Int.MIN_VALUE }
        dp[0] = 0
        for(i in 1 until n) {
            for(j in 0 until i) {
                if((nums[i] - nums[j]).absoluteValue <= target) {
                    dp[i] = maxOf(dp[i], dp[j] + 1)
                }
            }
        }
        return if (dp[n-1]<0) -1 else dp[n-1]
    }
}
// @lc code=end

