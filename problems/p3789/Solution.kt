package p3789

/*
 * @lc app=leetcode id=3789 lang=kotlin
 *
 * [3789] Minimum Cost to Acquire Required Items
 *
 * https://leetcode.com/problems/minimum-cost-to-acquire-required-items/description/
 *
 * algorithms
 * Medium (35.17%)
 * Likes:    76
 * Dislikes: 6
 * Total Accepted:    29.5K
 * Total Submissions: 78.4K
 * Testcase Example:  '3\n2\n1\n3\n2'
 *
 * You are given five integers cost1, cost2, costBoth, need1, and need2.
 * 
 * There are three types of items available:
 * 
 * 
 * An item of type 1 costs cost1 and contributes 1 unit to the type 1
 * requirement only.
 * An item of type 2 costs cost2 and contributes 1 unit to the type 2
 * requirement only.
 * An item of type 3 costs costBoth and contributes 1 unit to both type 1 and
 * type 2 requirements.
 * 
 * 
 * You must collect enough items so that the total contribution toward type 1
 * is at least need1 and the total contribution toward type 2 is at least
 * need2.
 * 
 * Return an integer representing the minimum possible total cost to achieve
 * these requirements.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: cost1 = 3, cost2 = 2, costBoth = 1, need1 = 3, need2 = 2
 * 
 * Output: 3
 * 
 * Explanation:
 * 
 * After buying three type 3 items, which cost 3 * 1 = 3, the total
 * contribution to type 1 is 3 (>= need1 = 3) and to type 2 is 3 (>= need2 =
 * 2).
 * Any other valid combination would cost more, so the minimum total cost is
 * 3.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: cost1 = 5, cost2 = 4, costBoth = 15, need1 = 2, need2 = 3
 * 
 * Output: 22
 * 
 * Explanation:
 * 
 * We buy need1 = 2 items of type 1 and need2 = 3 items of type 2: 2 * 5 + 3 *
 * 4 = 10 + 12 = 22.
 * Any other valid combination would cost more, so the minimum total cost is
 * 22.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: cost1 = 5, cost2 = 4, costBoth = 15, need1 = 0, need2 = 0
 * 
 * Output: 0
 * 
 * Explanation:
 * 
 * Since no items are required (need1 = need2 = 0), we buy nothing and pay
 * 0.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= cost1, cost2, costBoth <= 10^6
 * 0 <= need1, need2 <= 10^9
 * 
 * 
 */

// @lc code=start
class Solution {
    fun minimumCost(cost1: Int, cost2: Int, costBoth: Int, need1: Int, need2: Int): Long {
        val common = minOf(need1, need2).toLong()
        val remaining1 = need1 - common
        val remaining2 = need2 - common

        return common * minOf(cost1 + cost2, costBoth) +
            remaining1 * minOf(cost1, costBoth) +
            remaining2 * minOf(cost2, costBoth)
    }
}
// @lc code=end

