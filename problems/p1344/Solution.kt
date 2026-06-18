package p1344

import kotlin.math.abs
import kotlin.math.min

/*
 * @lc app=leetcode id=1344 lang=kotlin
 *
 * [1344] Angle Between Hands of a Clock
 */

// @lc code=start
class Solution {
    fun angleClock(hour: Int, minutes: Int): Double {
        val rand = 360.0
        val hourAngle = (hour % 12 * 30 + minutes * 0.5)
        val minuteAngle = minutes * 6
        val diff = abs(hourAngle - minuteAngle)
        return min(diff, rand - diff)
    }
}
// @lc code=end

