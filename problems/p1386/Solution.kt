package p1386

/*
 * @lc app=leetcode id=1386 lang=kotlin
 *
 * [1386] Cinema Seat Allocation
 */

// @lc code=start
class Solution {
    fun maxNumberOfFamilies(n: Int, reservedSeats: Array<IntArray>): Int {
        val map = mutableMapOf<Int, Int>()
        for (seat in reservedSeats) {
            val row = seat[0]
            val col = seat[1]
            map[row] = (map.getOrDefault(row, 0) or (1 shl (col - 1)))
        }
        var ans = 0
        val emptyRows = n - map.size
        ans += emptyRows * 2

        val leftMask = 0b0000011110   // 第 2~5 列
        val middleMask = 0b0001111000 // 第 4~7 列
        val rightMask = 0b0111100000  // 第 6~9 列

        map.values.forEach { mask ->
            val canUseLeft = (mask and leftMask) == 0
            val canUseMiddle = (mask and middleMask) == 0
            val canUseRight = (mask and rightMask) == 0

            ans += when {
                canUseLeft && canUseRight -> 2
                canUseLeft || canUseMiddle || canUseRight -> 1
                else -> 0
            }
        }
        return ans
    }
}
// @lc code=end
