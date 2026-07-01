package p2812

import java.util.PriorityQueue

/*
 * @lc app=leetcode id=2812 lang=kotlin
 *
 * [2812] Find the Safest Path in a Grid
 */

// @lc code=start

class Solution {
    private data class Position(val row: Int, val col: Int)

    private data class PathState(
        val row: Int,
        val col: Int,
        val safeness: Int,
    )

    private val directions = arrayOf(
        -1 to 0,
        1 to 0,
        0 to -1,
        0 to 1,
    )

    fun maximumSafenessFactor(grid: List<List<Int>>): Int {
        val safetyMatrix = buildSafetyMatrix(grid)
        return findSafestPath(safetyMatrix)
    }

    /**
     * 从所有小偷的位置同时进行 BFS。
     *
     * BFS 第一次到达某个格子时走过的步数，就是该格子到最近小偷的距离。
     */
    private fun buildSafetyMatrix(grid: List<List<Int>>): Array<IntArray> {
        val rows = grid.size
        val cols = grid[0].size
        val safety = Array(rows) { IntArray(cols) { -1 } }
        val queue = ArrayDeque<Position>()

        for (row in 0 until rows) {
            for (col in 0 until cols) {
                if (grid[row][col] == 1) {
                    safety[row][col] = 0
                    queue.addLast(Position(row, col))
                }
            }
        }

        while (queue.isNotEmpty()) {
            val current = queue.removeFirst()

            for ((rowOffset, colOffset) in directions) {
                val nextRow = current.row + rowOffset
                val nextCol = current.col + colOffset

                if (isInside(nextRow, nextCol, rows, cols) && safety[nextRow][nextCol] == -1) {
                    safety[nextRow][nextCol] = safety[current.row][current.col] + 1
                    queue.addLast(Position(nextRow, nextCol))
                }
            }
        }

        return safety
    }

    /**
     * 最大堆优先扩展当前安全系数最高的路径。
     * 一条路径的安全系数，是路径上所有格子安全距离的最小值。
     */
    private fun findSafestPath(safety: Array<IntArray>): Int {
        val rows = safety.size
        val cols = safety[0].size
        val bestSafeness = Array(rows) { IntArray(cols) { -1 } }
        val maxHeap = PriorityQueue<PathState>(compareByDescending { it.safeness })

        bestSafeness[0][0] = safety[0][0]
        maxHeap.add(PathState(0, 0, safety[0][0]))

        while (maxHeap.isNotEmpty()) {
            val current = maxHeap.poll()

            // 堆里可能还留有同一格子的旧状态。
            if (current.safeness < bestSafeness[current.row][current.col]) continue
            if (current.row == rows - 1 && current.col == cols - 1) {
                return current.safeness
            }

            for ((rowOffset, colOffset) in directions) {
                val nextRow = current.row + rowOffset
                val nextCol = current.col + colOffset

                if (!isInside(nextRow, nextCol, rows, cols)) continue

                val nextSafeness = minOf(current.safeness, safety[nextRow][nextCol])
                if (nextSafeness > bestSafeness[nextRow][nextCol]) {
                    bestSafeness[nextRow][nextCol] = nextSafeness
                    maxHeap.add(PathState(nextRow, nextCol, nextSafeness))
                }
            }
        }

        return 0
    }

    private fun isInside(row: Int, col: Int, rows: Int, cols: Int): Boolean {
        return row in 0 until rows && col in 0 until cols
    }
}

// @lc code=end
