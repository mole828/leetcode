package problems.p1391
/*
 * @lc app=leetcode id=1391 lang=kotlin
 *
 * [1391] Check if There is a Valid Path in a Grid
 */

// @lc code=start
class Solution {
    fun hasValidPath(grid: Array<IntArray>): Boolean {
        val m = grid.size
        val n = grid[0].size
        val dx = intArrayOf(-1, 0, 1, 0)
        val dy = intArrayOf(0, 1, 0, -1)
        val masks = intArrayOf(
            0,
            0b1010, // left, right
            0b0101, // up, down
            0b1100, // left, down
            0b0110, // right, down
            0b1001, // left, up
            0b0011, // right, up
        )

        val visited = Array(m) { BooleanArray(n) }
        val queue = ArrayDeque<Int>()
        queue.add(0)
        visited[0][0] = true

        while (queue.isNotEmpty()) {
            val cur = queue.removeFirst()
            val x = cur / n
            val y = cur % n

            if (x == m - 1 && y == n - 1) return true

            val mask = masks[grid[x][y]]
            for (dir in 0 until 4) {
                if (mask and (1 shl dir) == 0) continue

                val nextX = x + dx[dir]
                val nextY = y + dy[dir]
                if (nextX !in 0 until m || nextY !in 0 until n) continue
                if (visited[nextX][nextY]) continue

                val back = (dir + 2) % 4
                if (masks[grid[nextX][nextY]] and (1 shl back) == 0) continue

                visited[nextX][nextY] = true
                queue.add(nextX * n + nextY)
            }
        }

        return false
    }
}
// @lc code=end
