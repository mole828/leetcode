package problems.p3783

import kotlin.math.absoluteValue

/*
 * @lc app=leetcode id=3783 lang=kotlin
 *
 * [3783] Mirror Distance of an Integer
 */
// @lc code=start
class Solution {
    fun mirrorDistance(n: Int): Int {
        return n.toString().reversed().toInt().minus(n).absoluteValue
    }
}
// @lc code=end

