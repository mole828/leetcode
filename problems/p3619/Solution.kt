package p3619

/*
 * @lc app=leetcode id=3619 lang=kotlin
 *
 * [3619] Count Islands With Total Value Divisible by K
 *
 * https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/description/
 *
 * algorithms
 * Medium (56.19%)
 * Likes:    90
 * Dislikes: 4
 * Total Accepted:    40K
 * Total Submissions: 69.5K
 * Testcase Example:  '[[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]]\n5'
 *
 * You are given an m x n matrix grid and a positive integer k. An island is a
 * group of positive integers (representing land) that are 4-directionally
 * connected (horizontally or vertically).
 * 
 * The total value of an island is the sum of the values of all cells in the
 * island.
 * 
 * Return the number of islands with a total value divisible by k.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]],
 * k = 5
 * 
 * Output: 2
 * 
 * Explanation:
 * 
 * The grid contains four islands. The islands highlighted in blue have a total
 * value that is divisible by 5, while the islands highlighted in red do not.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: grid = [[3,0,3,0], [0,3,0,3], [3,0,3,0]], k = 3
 * 
 * Output: 6
 * 
 * Explanation:
 * 
 * The grid contains six islands, each with a total value that is divisible by
 * 3.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * m == grid.length
 * n == grid[i].length
 * 1 <= m, n <= 1000
 * 1 <= m * n <= 10^5
 * 0 <= grid[i][j] <= 10^6
 * 1 <= k <= 10^6
 * 
 * 
 */

// @lc code=start
class Solution {
    data class Place(val y: Int, val x: Int)
    fun countIslands(grid: Array<IntArray>, k: Int): Int {
        fun Place.isVaild() = (y in grid.indices) and (x in grid.first().indices)
        fun Place.getValue() = grid[y][x]
        val que = mutableListOf<Place>()
        grid.forEachIndexed { y, row -> row.forEachIndexed { x, v -> 
            if (v > 0) que.add(Place(y,x))
        } }

        val p2g = mutableMapOf<Place, Int>()
        val groupSum = mutableListOf<Long>()
        var groupNum = 0

        while (que.isNotEmpty()) {
            val roundBegin = que.removeFirst()
            if (roundBegin in p2g) continue
            groupSum.add(0L)
            val thisRound = mutableListOf(roundBegin)
            while (thisRound.isNotEmpty()) {
                val p = thisRound.removeFirst()
                if (p in p2g) continue
                if (p.isVaild() && p.getValue() > 0) {
                    p2g[p] = groupNum
                    groupSum[groupNum] += p.getValue()
                    val (y,x) = p
                    thisRound.add(p.copy(y=y+1))
                    thisRound.add(p.copy(y=y-1))
                    thisRound.add(p.copy(x=x+1))
                    thisRound.add(p.copy(x=x-1))
                }
            }
            groupNum += 1
        }

        return groupSum.filter { it % k == 0L }.size
    }
}
// @lc code=end

