package p1288

/*
 * @lc app=leetcode id=1288 lang=kotlin
 *
 * [1288] Remove Covered Intervals
 */

// @lc code=start
class Solution {
    fun removeCoveredIntervals(intervals: Array<IntArray>): Int {
        intervals.sortWith(
            compareBy<IntArray> { it[0] }
                .thenByDescending { it[1] }
        )

        var maxEnd = -1
        var count = 0

        for (interval in intervals) {
            if (interval[1] > maxEnd) {
                count++
                maxEnd = interval[1]
            }
        }

        return count
    }
}
// @lc code=end

fun main() {
    val solution = Solution()
    val intervals1 = arrayOf(intArrayOf(1, 4), intArrayOf(3, 6), intArrayOf(2, 8))
    println(solution.removeCoveredIntervals(intervals1)) // Output: 2
}