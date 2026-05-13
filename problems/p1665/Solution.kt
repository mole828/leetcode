package p1665
/*
 * @lc app=leetcode id=1665 lang=kotlin
 *
 * [1665] Minimum Initial Energy to Finish Tasks
 */

// @lc code=start
class Solution {
    fun minimumEffort(tasks: Array<IntArray>): Int {
        val tasks = tasks.map { it[0] to it[1] }.sortedByDescending { it.first - it.second }
        return tasks.fold(0) { acc, (actual, minimum) ->
            maxOf(acc + actual, minimum)
        }
    }
}
// @lc code=end

