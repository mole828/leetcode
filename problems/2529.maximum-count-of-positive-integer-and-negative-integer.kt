/*
 * @lc app=leetcode id=2529 lang=kotlin
 *
 * [2529] Maximum Count of Positive Integer and Negative Integer
 */
package p2529

// @lc code=start
class Solution {
    fun maximumCount(nums: IntArray): Int {
        return maxOf(
            nums.count {it<0},
            nums.count {it>0},
        )
    }
}
// @lc code=end

