package problems.p3070
/*
 * @lc app=leetcode id=3070 lang=kotlin
 *
 * [3070] Count Submatrices with Top-Left Element and Sum Less Than k
 */

// @lc code=start
class Solution {
    fun countSubmatrices(grid: Array<IntArray>, k: Int): Int {
        val sumGrid = Array(grid.size+1){IntArray(grid.first().size+1)}
        var count = 0
        sumGrid.forEachIndexed { i, row ->
            if(i>0){
                row.forEachIndexed { j, _ ->
                    if(j>0){
                        val newSum = sumGrid[i-1][j] + sumGrid[i][j-1] - sumGrid[i-1][j-1] + grid[i-1][j-1]
                        sumGrid[i][j] = newSum
                        if(newSum <= k){
                            count++
                        }
                    }
                }
            }
        }
        return count
    }
}
// @lc code=end

