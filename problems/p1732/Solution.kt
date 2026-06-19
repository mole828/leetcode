package p1732
/*
 * @lc app=leetcode id=1732 lang=kotlin
 *
 * [1732] Find the Highest Altitude
 */
// @lc code=start
class Solution {
    fun largestAltitude(gain: IntArray): Int {
        var highest = 0
        var altitude = 0
        for (g in gain) {
            altitude += g
            if (altitude > highest) highest = altitude
        }
        return highest
    }
}
// @lc code=end

