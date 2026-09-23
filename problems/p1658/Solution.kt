package p1658

/*
 * @lc app=leetcode id=1658 lang=kotlin
 *
 * [1658] Minimum Operations to Reduce X to Zero
 */

// @lc code=start
class Solution {
    fun minOperations(nums: IntArray, x: Int): Int {
        val target = nums.sum() - x
        if (target < 0) return -1
        if (target == 0) return nums.size

        var left = 0
        var sum = 0
        var maxLength = -1
        for (right in nums.indices) {
            sum += nums[right]
            while (sum > target) {
                sum -= nums[left++]
            }
            if (sum == target) {
                maxLength = maxOf(maxLength, right - left + 1)
            }
        }
        return if (maxLength == -1) -1 else nums.size - maxLength
    }
}
// @lc code=end

