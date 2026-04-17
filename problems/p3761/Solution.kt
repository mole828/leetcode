package problems.p3761

/*
 * @lc app=leetcode id=3761 lang=kotlin
 *
 * [3761] Minimum Absolute Distance Between Mirror Pairs
 */

// @lc code=start
class Solution {
    fun minMirrorPairDistance(nums: IntArray): Int {
        val inf = 100_000_000
        var minDistance = inf
        val reverseMap = mutableMapOf<Int, MutableList<Int>>()
        nums.forEachIndexed { ia, va ->
            val meeted = reverseMap.getOrPut(va) { mutableListOf() }
            if (meeted.isNotEmpty()) {
                val ib = meeted.last()
                minDistance = minOf(minDistance, ia - ib)
            }
            val reverseValue = va.toString().reversed().toInt()
            reverseMap.getOrPut(reverseValue) { mutableListOf() }.add(ia)
        }
        return if (minDistance == inf) -1 else minDistance
    }
}
// @lc code=end

