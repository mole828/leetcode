/*
 * @lc app=leetcode id=2579 lang=kotlin
 *
 * [2579] Count Total Number of Colored Cells
 */
package p2579

// @lc code=start
class Solution {
    fun coloredCells(n: Int): Long {
        return (n.downTo(1)).sumOf { 
            4L * (it - 1) 
        } + 1
    }
}
// @lc code=end

fun main() {
    println(Solution().coloredCells(3))
}