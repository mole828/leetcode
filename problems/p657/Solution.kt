package problems.p657
/*
 * @lc app=leetcode id=657 lang=kotlin
 *
 * [657] Robot Return to Origin
 */
// @lc code=start
class Solution {
    fun judgeCircle(moves: String): Boolean {
        var x = 0
        var y = 0
        for (move in moves) {
            when (move) {
                'U' -> y++
                'D' -> y--
                'L' -> x--
                'R' -> x++
            }
        }
        return x == 0 && y == 0
    }
}
// @lc code=end

