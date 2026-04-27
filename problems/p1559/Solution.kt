package problems.p1559
/*
 * @lc app=leetcode id=1559 lang=kotlin
 *
 * [1559] Detect Cycles in 2D Grid
 */

// @lc code=start
class Solution {
    fun containsCycle(grid: Array<CharArray>): Boolean {
        val m = grid.size
        val n = grid[0].size
        val visited = Array(m) { BooleanArray(n) }
        val dirs = intArrayOf(1, 0, -1, 0, 1)

        for (i in 0 until m) {
            for (j in 0 until n) {
                if (visited[i][j]) continue

                val stack = ArrayDeque<IntArray>()
                stack.add(intArrayOf(i, j, -1, -1))
                visited[i][j] = true

                while (stack.isNotEmpty()) {
                    val cur = stack.removeLast()
                    val x = cur[0]
                    val y = cur[1]
                    val parentX = cur[2]
                    val parentY = cur[3]

                    for (k in 0 until 4) {
                        val nextX = x + dirs[k]
                        val nextY = y + dirs[k + 1]

                        if (nextX !in 0 until m || nextY !in 0 until n) continue
                        if (grid[nextX][nextY] != grid[x][y]) continue
                        if (nextX == parentX && nextY == parentY) continue

                        if (visited[nextX][nextY]) {
                            return true
                        }

                        visited[nextX][nextY] = true
                        stack.add(intArrayOf(nextX, nextY, x, y))
                    }
                }
            }
        }

        return false
    }
}
// @lc code=end
