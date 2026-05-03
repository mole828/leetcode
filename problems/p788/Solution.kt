package problems.p788
/*
 * @lc app=leetcode id=788 lang=kotlin
 *
 * [788] Rotated Digits
 */
// @lc code=start
class Solution {
    fun isGood(n: Int): Boolean = 
        n.toString().fold(false) { changed, c ->
        when (c) {
            '3', '4', '7' -> return false
            '2', '5', '6', '9' -> true
            else -> changed
        }
    }
    fun rotatedDigits(n: Int) = (1..n).count { isGood(it) }
}
// @lc code=end

