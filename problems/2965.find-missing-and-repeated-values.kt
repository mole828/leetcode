package p2965
/*
 * @lc app=leetcode id=2965 lang=kotlin
 *
 * [2965] Find Missing and Repeated Values
 */


// @lc code=start
class Solution {
    fun findMissingAndRepeatedValues(grid: Array<IntArray>): IntArray {
        val nums = grid.flatMap { it.toList() }
        val hasSet = nums.toSet()
        val shouldSet = (1..nums.size).toSet()
        val missing = shouldSet.minus(hasSet).first()
        val repeated = nums.groupBy { it }.filter { it.value.size > 1 }.keys.first()
        return intArrayOf(repeated, missing)
    }
}
// @lc code=end

fun main() {
    println(Solution().findMissingAndRepeatedValues(arrayOf(intArrayOf(1, 3), intArrayOf(2, 2))))
}
