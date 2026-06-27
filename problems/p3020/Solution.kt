package p3020
/*
 * @lc app=leetcode id=3020 lang=kotlin
 *
 * [3020] Find the Maximum Number of Elements in Subset
 */
// @lc code=start
class Solution {
    fun maximumLength(nums: IntArray): Int {
        val counts = mutableMapOf<Int, Int>()
        for (num in nums) {
            counts[num] = counts.getOrDefault(num, 0) + 1
        }
        var ans = (counts.getOrDefault(1, 0) - 1) or 1
        counts.remove(1)
        for (num in counts.keys) {
            var num = num
            var res = 0
            while (counts.getOrDefault(num, 0) >= 2) {
                res += 2
                num *= num
            }
            ans = maxOf(ans, res + (if (num in counts) 1 else -1))
        }
        return ans
    }
}
// @lc code=end

