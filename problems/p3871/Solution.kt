package p3871

/*
 * @lc app=leetcode id=3871 lang=kotlin
 *
 * [3871] Count Commas in Range II
 */

// @lc code=start
class Solution {
    fun countCommas(n: Long): Long {
        // 1 <= n <= 10^15
        var n = n
        var count = 0L
        if (n > 999_999_999_999_999L) {
            count += (n - 999_999_999_999_999L) * 5
            n = 999_999_999_999_999L
        }
        if (n > 999_999_999_999L) {
            count += (n - 999_999_999_999L) * 4
            n = 999_999_999_999L
        }
        if (n > 999_999_999L) {
            count += (n - 999_999_999L) * 3
            n = 999_999_999L
        }
        if (n > 999_999L) {
            count += (n - 999_999L) * 2
            n = 999_999L
        }
        if (n > 999L) {
            count += (n - 999L) * 1
            n = 999L
        }
        return count
    }
}
// @lc code=end
