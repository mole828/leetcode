package p3904
/*
 * @lc app=leetcode id=3904 lang=kotlin
 *
 * [3904] Smallest Stable Index II
 */
// @lc code=start
class Solution {
    fun firstStableIndex(nums: IntArray, k: Int): Int {
        val minRight = IntArray(nums.size) { 0 }
        minRight[nums.lastIndex] = nums[nums.lastIndex]
        for (i in nums.indices.reversed()) {
            minRight[i] = if (i == nums.lastIndex) nums[i] else minOf(nums[i], minRight[i + 1])
        }
        var prevMax = Int.MIN_VALUE
        for (i in nums.indices) {
            prevMax = maxOf(prevMax, nums[i])
            if (prevMax - minRight[i] <= k) return i
        }
        return -1
    }
}
// @lc code=end

