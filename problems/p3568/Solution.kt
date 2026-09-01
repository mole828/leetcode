package p3568

/*
 * @lc app=leetcode id=3568 lang=kotlin
 *
 * [3568] Minimum Moves to Clean the Classroom
 */

// @lc code=start
class Solution {
    data class State(
        val x: Int,
        val y: Int,
        val e: Int,
        val mask: Int
    )

    fun minMoves(classroom: Array<String>, energy: Int): Int {
        val m = classroom.size
        val n = classroom[0].length

        val litterIndex = Array(m) { IntArray(n) { -1 } }

        var start = 0 to 0
        var litterCount = 0

        classroom.forEachIndexed { x, row ->
            row.forEachIndexed { y, c ->
                when (c) {
                    'S' -> start = x to y
                    'L' -> litterIndex[x][y] = litterCount++
                }
            }
        }

        if (litterCount == 0) return 0

        val target = (1 shl litterCount) - 1
        val visited = Array(m * n) {
            IntArray(1 shl litterCount) { -1 }
        }

        val queue = ArrayDeque<State>().apply {
            add(State(start.first, start.second, energy, 0))
        }

        visited[start.first * n + start.second][0] = energy

        val dirs = arrayOf(
            -1 to 0,
            1 to 0,
            0 to -1,
            0 to 1
        )

        var moves = 0

        while (queue.isNotEmpty()) {
            repeat(queue.size) {
                val (x, y, e, mask) = queue.removeFirst()

                if (mask == target) return moves
                if (e == 0) return@repeat

                for ((dx, dy) in dirs) {
                    val nx = x + dx
                    val ny = y + dy

                    if (nx !in classroom.indices ||
                        ny !in classroom[0].indices ||
                        classroom[nx][ny] == 'X'
                    ) continue

                    val cell = classroom[nx][ny]

                    val ne = if (cell == 'R') energy else e - 1

                    val nm = if (cell == 'L') {
                        mask or (1 shl litterIndex[nx][ny])
                    } else {
                        mask
                    }

                    if (nm == target) return moves + 1

                    val pos = nx * n + ny

                    if (visited[pos][nm] >= ne) continue

                    visited[pos][nm] = ne
                    queue += State(nx, ny, ne, nm)
                }
            }

            moves++
        }

        return -1
    }
}
// @lc code=end

