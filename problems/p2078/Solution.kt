package problems.p2078
/*
 * @lc app=leetcode id=2078 lang=kotlin
 *
 * [2078] Two Furthest Houses With Different Colors
 */

// @lc code=start
class Solution {
    fun maxDistance(colors: IntArray): Int {
        val n = colors.size
        val begin = mutableMapOf<Int, Int>()
        val end = mutableMapOf<Int, Int>()
        colors.forEachIndexed { i, c ->
            begin.putIfAbsent(c, i)
            end[c] = i
        }
        var maxDist = 0
        begin.keys.forEach { key1 ->
            end.keys.forEach { key2 ->
                if (key1 != key2) {
                    maxDist = listOf(
                        maxDist,
                        kotlin.math.abs(begin[key1]!! - end[key2]!!),
                        kotlin.math.abs(end[key1]!! - begin[key2]!!)
                    ).max()
                }
            }
        }
        return maxDist
    }
}
// @lc code=end

