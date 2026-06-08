package p2161

/*
 * @lc app=leetcode id=2161 lang=kotlin
 *
 * [2161] Partition Array According to Given Pivot
 */

// @lc code=start
class Solution {
    fun pivotArray(nums: IntArray, pivot: Int): IntArray {
        val less = mutableListOf<Int>()
        val equal = mutableListOf<Int>()
        val greater = mutableListOf<Int>()
        for (num in nums) {
            when {
                num < pivot -> less.add(num)
                num == pivot -> equal.add(num)
                else -> greater.add(num)
            }
        }
        return (less + equal + greater).toIntArray()
    }
}
// @lc code=end

