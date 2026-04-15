package problems.p2515
/*
 * @lc app=leetcode id=2515 lang=kotlin
 *
 * [2515] Shortest Distance to Target String in a Circular Array
 */

// @lc code=start
class Solution {
    fun closestTarget(words: Array<String>, target: String, startIndex: Int): Int {
        val n = words.size
        val words = words + words + words
        val startIndex = startIndex + n
        val targetIndices = words.withIndex().filter { it.value == target }.map { it.index }
        var minDistance = Int.MAX_VALUE
        for (index in targetIndices) {
            minDistance = minOf(minDistance, kotlin.math.abs(index - startIndex))
        }
        return if (minDistance == Int.MAX_VALUE) -1 else minDistance
    }
}
// @lc code=end

