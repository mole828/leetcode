package problems.p1878
/*
 * @lc app=leetcode id=1878 lang=kotlin
 *
 * [1878] Get Biggest Three Rhombus Sums in a Grid
 */
// @lc code=start
class Solution {
    fun getBiggestThree(grid: Array<IntArray>): IntArray {
        val m = grid.size
        val n = grid[0].size
        val diagSum = Array(m + 1) { IntArray(n  + 1) }
        val antiDiagSum = Array(m + 1) { IntArray(n + 1) }
        for (i in 0 until m) {
            for (j in 0 until n) {
                val v = grid[i][j]
                diagSum[i + 1][j + 1] = diagSum[i][j] + v
                antiDiagSum[i + 1][j] = antiDiagSum[i][j+1] + v
            }
        }
        fun queryDiagonal(x: Int, y: Int, k: Int): Int {
            return diagSum[x+k][y+k] - diagSum[x][y]
        }
        fun queryAntiDiagonal(x: Int, y: Int, k: Int): Int {
            return antiDiagSum[x+k][y+1-k] - antiDiagSum[x][y+1]
        }
        val sums = mutableListOf<Int>()

        // 辅助函数：更新并保持前三大的不同值
        fun addSum(value: Int) {
            if (value !in sums) {
                sums.add(value)
                // 仅在数据较多时排序并截取，保持高效
                if (sums.size > 10) { 
                    sums.sortDescending()
                    // 只要前三个
                    val topThree = sums.take(3).toMutableList()
                    sums.clear()
                    sums.addAll(topThree)
                }
            }
        }
        grid.forEachIndexed { i, row ->
            row.forEachIndexed { j, v ->
                addSum(v)
                val mx = listOf(i, m-1-i, j, n-1-j).min()
                for (k in 1..mx) {
                    addSum(
                        listOf(
                            queryDiagonal(i-k, j, k),
                            queryDiagonal(i, j-k, k),
                            queryAntiDiagonal(i-k+1, j-1, k-1),
                            queryAntiDiagonal(i, j+k, k+1)
                        ).sum()
                    )
                }
            }
        }
        
        return sums.sortedDescending().take(3).toIntArray()
    }
}
// @lc code=end

// [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
