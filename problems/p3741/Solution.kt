package problems.p3741
/*
 * @lc app=leetcode id=3741 lang=kotlin
 *
 * [3741] Minimum Distance Between Three Equal Elements II
 */
// @lc code=start
class Solution {
    fun minimumDistance(nums: IntArray): Int {
        val positions = mutableMapOf<Int, MutableList<Int>>()
        nums.forEachIndexed { index, value ->
            positions.computeIfAbsent(value) { mutableListOf() }.add(index)
        }
        // Find the minimum distance between three equal elements
        var minDistance = Int.MAX_VALUE
        positions.map { 
            val posList = it.value
            while (posList.size >= 3) {
                val (a,b,c) = posList
                val dist = (b - a) + (c - b) + (c - a)
                minDistance = minOf(minDistance, dist)
                posList.removeAt(0)
            }
        }
        return if (minDistance == Int.MAX_VALUE) -1 else minDistance
    }
}
// @lc code=end

