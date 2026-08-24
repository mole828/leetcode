package p1872

/*
 * @lc app=leetcode id=1872 lang=kotlin
 *
 * [1872] Stone Game VIII
 */

// @lc code=start
class Solution {
    fun stoneGameVIII(stones: IntArray): Int {
        val n = stones.size
        val prefixSum = IntArray(n)
        prefixSum[0] = stones[0]
        for (i in 1 until n) {
            prefixSum[i] = prefixSum[i - 1] + stones[i]
        }

        var best = prefixSum[n - 1]
        for (i in n - 2 downTo 1) {
            best = maxOf(best, prefixSum[i] - best)
        }

        return best
    }
}
// @lc code=end
