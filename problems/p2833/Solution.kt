package problems.p2833
/*
 * @lc app=leetcode id=2833 lang=kotlin
 *
 * [2833] Furthest Point From Origin
 */

// @lc code=start
class Solution {
    fun furthestDistanceFromOrigin(moves: String): Int {
        val blankCount = moves.count { it == '_' }
        val lCount = moves.count { it == 'L' }
        val rCount = moves.count { it == 'R' }
        return maxOf(lCount + blankCount - rCount, rCount + blankCount - lCount)
    }
}
// @lc code=end

