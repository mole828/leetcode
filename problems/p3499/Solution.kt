package p3499

/*
 * @lc app=leetcode id=3499 lang=kotlin
 *
 * [3499] Maximize Active Section with Trade I
 */

// @lc code=start
class Solution {
    fun maxActiveSectionsAfterTrade(s: String): Int {
        var maxActive = 0
        var preZeroCount = Int.MIN_VALUE
        var count = 0
        var ans = 0
        s.forEachIndexed { i, char ->
            count++
            if (i==s.length -1 || char != s[i+1]) {
                if (char == '1') {
                    ans += count
                } else {
                    maxActive = maxOf(maxActive, preZeroCount + count)
                    preZeroCount = count
                }
                count = 0
            }
        }
        return ans + maxActive
    }
}
// @lc code=end

