package p3882

/*
 * @lc app=leetcode id=3882 lang=kotlin
 *
 * [3882] Minimum XOR Path in a Grid
 *
 * https://leetcode.com/problems/minimum-xor-path-in-a-grid/description/
 *
 * algorithms
 * Medium (39.86%)
 * Likes:    86
 * Dislikes: 6
 * Total Accepted:    22.2K
 * Total Submissions: 51.6K
 * Testcase Example:  '[[1,2],[3,4]]'
 *
 * You are given a 2D integer array grid of size m * n.
 * 
 * You start at the top-left cell (0, 0) and want to reach the bottom-right
 * cell (m - 1, n - 1).
 * 
 * At each step, you may move either right or down.
 * 
 * The cost of a path is defined as the bitwise XOR of all the values in the
 * cells along that path, including the start and end cells.
 * 
 * Return the minimum possible XOR value among all valid paths from (0, 0) to
 * (m - 1, n - 1).
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: grid = [[1,2],[3,4]]
 * 
 * Output: 6
 * 
 * Explanation:
 * 
 * There are two valid paths:
 * 
 * 
 * (0, 0) → (0, 1) → (1, 1) with XOR: 1 XOR 2 XOR 4 = 7
 * (0, 0) → (1, 0) → (1, 1) with XOR: 1 XOR 3 XOR 4 = 6
 * 
 * 
 * The minimum XOR value among all valid paths is 6.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: grid = [[6,7],[5,8]]
 * 
 * Output: 9
 * 
 * Explanation:
 * 
 * There are two valid paths:
 * 
 * 
 * (0, 0) → (0, 1) → (1, 1) with XOR: 6 XOR 7 XOR 8 = 9
 * (0, 0) → (1, 0) → (1, 1) with XOR: 6 XOR 5 XOR 8 = 11
 * 
 * 
 * The minimum XOR value among all valid paths is 9.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: grid = [[2,7,5]]
 * 
 * Output: 0
 * 
 * Explanation:
 * 
 * There is only one valid path:
 * 
 * 
 * (0, 0) → (0, 1) → (0, 2) with XOR: 2 XOR 7 XOR 5 = 0
 * 
 * 
 * The XOR value of this path is 0, which is the minimum possible.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= m == grid.length <= 1000
 * 1 <= n == grid[i].length <= 1000
 * m * n <= 1000
 * 0 <= grid[i][j] <= 1023​
 * 
 * 
 */

// @lc code=start
class Solution {
    fun minCost(grid: Array<IntArray>): Int {
        val memo = Array(grid.size) {
            arrayOfNulls<BooleanArray>(grid.first().size)
        }
        memo.last()[grid.last().lastIndex] = BooleanArray(1024).apply {
            this[grid.last().last()] = true
        }

        fun dfs(y: Int, x: Int): BooleanArray {
            memo[y][x]?.let { return it }

            val value = grid[y][x]
            val reachable = BooleanArray(1024)
            if (y + 1 in grid.indices) {
                dfs(y + 1, x).forEachIndexed { state, canReach ->
                    if (canReach) reachable[state xor value] = true
                }
            }
            if (x + 1 in grid.first().indices) {
                dfs(y, x + 1).forEachIndexed { state, canReach ->
                    if (canReach) reachable[state xor value] = true
                }
            }
            memo[y][x] = reachable
            return reachable
        }

        return dfs(0, 0).indexOfFirst { it }
    }
}
// @lc code=end

