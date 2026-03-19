package problems.p3212
/*
 * @lc app=leetcode id=3212 lang=kotlin
 *
 * [3212] Count Submatrices With Equal Frequency of X and Y
 */

// @lc code=start
class Solution {
    operator fun Pair<Int, Int>.plus(other: Pair<Int, Int>): Pair<Int, Int> {
        return Pair(this.first + other.first, this.second + other.second)
    }
    operator fun Pair<Int, Int>.minus(other: Pair<Int, Int>): Pair<Int, Int> {
        return Pair(this.first - other.first, this.second - other.second)
    }
    fun numberOfSubmatrices(grid: Array<CharArray>): Int {
        val charMap = mapOf(
            'X' to Pair(1,0), 
            'Y' to Pair(0,1),
            '.' to Pair(0,0),
        )
        val sumGrid = Array(grid.size+1){Array(grid.first().size+1){Pair(0,0)}}
        var count = 0
        sumGrid.forEachIndexed { i, row ->
            if(i>0){
                row.forEachIndexed { j, _ ->
                    if(j>0){
                        val newSum = sumGrid[i-1][j] + sumGrid[i][j-1] - sumGrid[i-1][j-1] + charMap.getOrDefault(grid[i-1][j-1], Pair(0,0))
                        sumGrid[i][j] = newSum
                        if(newSum.first>0 && newSum.first == newSum.second){
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

