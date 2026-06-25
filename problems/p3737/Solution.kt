package p3737

/*
 * @lc app=leetcode id=3737 lang=kotlin
 *
 * [3737] Count Subarrays With Majority Element I
 */

// @lc code=start
class Solution {
    fun countMajoritySubarrays(nums: IntArray, target: Int): Int {
        val countArray = IntArray(nums.size + 1)
        countArray[0] = 0
        for (i in nums.indices) {
            countArray[i + 1] = countArray[i] + if (nums[i] == target) 1 else 0
        }
        var result = 0
        for (i in nums.indices) {
            for (j in i until nums.size) {
                val count = countArray[j + 1] - countArray[i]
                if (count > (j - i + 1) / 2) {
                    result++
                }
            }
        }
        return result
    }
}
// @lc code=end

