package p3524

/*
 * @lc app=leetcode id=3524 lang=kotlin
 *
 * [3524] Find X Value of Array I
 */

// @lc code=start
class Solution {
    fun resultArray(nums: IntArray, k: Int): LongArray {
        val result = LongArray(k)
        var dp = LongArray(k)
        for (i in nums.indices) {
            val ndp = LongArray(k)
            ndp[nums[i] % k] += 1
            
            for (r in 0 until k) {
                val newR = (r * (nums[i] % k)) % k
                ndp[newR] += dp[r]
            }
            dp = ndp
            
            for (r in 0 until k) {
                result[r] += dp[r]
            }
        }
        return result
    }
}
// @lc code=end

