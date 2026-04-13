package problems.p1848
/*
 * @lc app=leetcode id=1848 lang=kotlin
 *
 * [1848] Minimum Distance to the Target Element
 */

// @lc code=start
class Solution {
    fun getMinDistance(nums: IntArray, target: Int, start: Int): Int {
        var minDistance = Int.MAX_VALUE
        nums.forEachIndexed { index, value ->
            if (value == target) {
                val dist = kotlin.math.abs(index - start)
                minDistance = minOf(minDistance, dist)
            }
        }
        return minDistance
    }
}
// @lc code=end

