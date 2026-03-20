package problems.p3567
/*
 * @lc app=leetcode id=3567 lang=kotlin
 *
 * [3567] Minimum Absolute Difference in Sliding Submatrix
 */

// @lc code=start
class Solution {
    fun minAbsDiff(grid: Array<IntArray>, k: Int): Array<IntArray> {
        val m = grid.size
        val n = grid.first().size
        val ans = Array(m-k+1){IntArray(n-k+1)}
        ans.forEachIndexed { i, row ->
            row.forEachIndexed { j, _ ->
                val subMatrix = mutableListOf<Int>()
                for(x in i until i+k){
                    for(y in j until j+k){
                        subMatrix.add(grid[x][y])
                    }
                }
                subMatrix.sort()
                var minDiff = Int.MAX_VALUE
                var hasChanged = false
                for(x in 1 until subMatrix.size){
                    val a = subMatrix[x-1]
                    val b = subMatrix[x]
                    if (a == b) continue
                    val diff = b-a
                    if (diff<minDiff){
                        minDiff = diff
                        hasChanged = true
                    }
                }
                println("subMatrix: $subMatrix, minDiff: $minDiff")
                ans[i][j] = if (hasChanged) minDiff else 0
            }
        }
        return ans
    }
}
// @lc code=end

