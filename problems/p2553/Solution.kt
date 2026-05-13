package p2553
/*
 * @lc app=leetcode id=2553 lang=kotlin
 *
 * [2553] Separate the Digits in an Array
 */

// @lc code=start
class Solution {
    fun separateDigits(nums: IntArray): IntArray {
        fun digits(num: Int): List<Int> {
            val ans = mutableListOf<Int>()
            var n = num
            while (n > 0) {
                ans.add(n % 10)
                n /= 10
            }
            return ans.reversed()
        }
        val result = mutableListOf<Int>()
        for (num in nums) {
            result.addAll(digits(num))
        }
        return result.toIntArray()
    }
}
// @lc code=end

