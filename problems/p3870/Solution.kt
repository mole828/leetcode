package p3870

/*
 * @lc app=leetcode id=3870 lang=kotlin
 *
 * [3870] Count Commas in Range
 */

// @lc code=start
class Solution {
    fun countCommas(n: Int): Int {
        return if (n > 999) n - 999 else 0
    }
}
// @lc code=end

