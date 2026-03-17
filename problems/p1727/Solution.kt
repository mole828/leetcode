package problems.p1727
/*
 * @lc app=leetcode id=1727 lang=kotlin
 *
 * [1727] Largest Submatrix With Rearrangements
 */

// @lc code=start
class Solution {
    fun largestSubmatrix(matrix: Array<IntArray>): Int {
        val n = matrix.first().size
        val heights = IntArray(n)
        var ans = 0
        matrix.forEach { row ->
            row.forEachIndexed{ j, x ->
                if(x==0){
                    heights[j] = 0
                } else {
                    heights[j] += 1
                }
            }
            val hs = heights.sorted()
            hs.forEachIndexed { i, h ->
                ans = maxOf(ans, (n-i)*h)
            }
        }
        return ans
    }
}
// @lc code=end

