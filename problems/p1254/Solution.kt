package p1254

/*
 * @lc app=leetcode id=1254 lang=kotlin
 *
 * [1254] Number of Closed Islands
 *
 * https://leetcode.com/problems/number-of-closed-islands/description/
 *
 * algorithms
 * Medium (67.29%)
 * Likes:    4832
 * Dislikes: 195
 * Total Accepted:    301.1K
 * Total Submissions: 445.1K
 * Testcase Example:  '[[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]'
 *
 * Given a 2D grid consists of 0s (land) and 1s (water).  An island is a
 * maximal 4-directionally connected group of 0s and a closed island is an
 * island totally (all left, top, right, bottom) surrounded by 1s.
 * 
 * Return the number of closed islands.
 * 
 * 
 * Example 1:
 * 
 * 
 * 
 * 
 * Input: grid =
 * [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
 * Output: 2
 * Explanation: 
 * Islands in gray are closed because they are completely surrounded by water
 * (group of 1s).
 * 
 * Example 2:
 * 
 * 
 * 
 * 
 * Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
 * Output: 1
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: grid = [[1,1,1,1,1,1,1],
 * [1,0,0,0,0,0,1],
 * [1,0,1,1,1,0,1],
 * [1,0,1,0,1,0,1],
 * [1,0,1,1,1,0,1],
 * [1,0,0,0,0,0,1],
 * ⁠              [1,1,1,1,1,1,1]]
 * Output: 2
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= grid.length, grid[0].length <= 100
 * 0 <= grid[i][j] <=1
 * 
 * 
 */

// @lc code=start
class Solution {
    data class Place(val y: Int, val x: Int)
    fun closedIsland(grid: Array<IntArray>): Int {
        val visited = mutableSetOf<Place>()
        fun Place.isValid(): Boolean =
            y in grid.indices && x in grid.first().indices
        fun Place.getValue(): Int = grid[y][x]
        fun bfs(start: Place): Boolean {
            val que = ArrayDeque<Place>()
            que.addLast(start)
            visited.add(start)
            var closed = true
            while (que.isNotEmpty()) {
                val place = que.removeFirst()
                val (y, x) = place
                listOf(
                    place.copy(y = y + 1),
                    place.copy(y = y - 1),
                    place.copy(x = x + 1),
                    place.copy(x = x - 1),
                ).forEach { next ->
                    if (!next.isValid()) {
                        closed = false
                    } else if (next.getValue() == 0 && visited.add(next)) {
                        que.addLast(next)
                    }
                }
            }
            return closed
        }

        var ans = 0
        grid.forEachIndexed { y, row ->
            row.forEachIndexed cell@ { x, v ->
                val place = Place(y, x)
                if (v != 0 || place in visited) return@cell
                if (bfs(place)) ans += 1
            }
        }
        return ans
    }
}
// @lc code=end

