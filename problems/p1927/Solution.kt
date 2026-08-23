package p1927
/*
 * @lc app=leetcode id=1927 lang=kotlin
 *
 * [1927] Sum Game
 */
// @lc code=start
class Solution {
    fun sumGame(num: String): Boolean {
        val left = num.substring(0, num.length / 2)
        val right = num.substring(num.length / 2)
        var sumDiff = 0
        val questionDiff = right.count { it == '?' } - left.count { it == '?' }

        for (digit in left) {
            if (digit != '?') {
                sumDiff += digit - '0'
            }
        }
        for (digit in right) {
            if (digit != '?') {
                sumDiff -= digit - '0'
            }
        }

        return 2 * sumDiff != 9 * questionDiff
    }
}
// @lc code=end
