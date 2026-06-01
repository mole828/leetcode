package p2144

/*
 * @lc app=leetcode id=2144 lang=kotlin
 *
 * [2144] Minimum Cost of Buying Candies With Discount
 */

// @lc code=start
class Solution {
    fun minimumCost(cost: IntArray): Int {
        cost.sortDescending()
        var ans = 0
        for (i in cost.indices) {
            if (i % 3 != 2) {
                ans += cost[i]
            }
        }
        return ans
    }
}
// @lc code=end

