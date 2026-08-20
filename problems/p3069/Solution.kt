package p3069

/*
 * @lc app=leetcode id=3069 lang=kotlin
 *
 * [3069] Distribute Elements Into Two Arrays I
 */

// @lc code=start
class Solution {
    fun resultArray(nums: IntArray): IntArray {
        val arr1 = mutableListOf<Int>(nums[0])
        val arr2 = mutableListOf<Int>(nums[1])
        for (i in 2 until nums.size) {
            if (arr1.last() > arr2.last()) arr1.add(nums[i])
            else arr2.add(nums[i])
        }
        return (arr1 + arr2).toIntArray()
    }
}
// @lc code=end

