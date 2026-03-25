package problems.p3546
/*
 * @lc app=leetcode id=3546 lang=kotlin
 *
 * [3546] Equal Sum Grid Partition I
 */

// @lc code=start
class Solution {
    fun canPartitionGrid(grid: Array<IntArray>): Boolean {
        val longGroup = grid.map { it.map { x -> x.toLong() } }
        val rowSums = longGroup.map { it.sum() }
        val colSums = longGroup[0].indices.map { j -> longGroup.sumOf { it[j] } }
        val totalSum = rowSums.sum()
        run {
            var sum = 0L
            for (s in rowSums) {
                sum += s
                if (sum * 2 == totalSum) return true
            }
        }
        run {
            var sum = 0L
            for (s in colSums) {
                sum += s
                if (sum * 2 == totalSum) return true
            }
        }
        return false
    }
}
// @lc code=end

