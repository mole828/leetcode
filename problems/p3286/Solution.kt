package p3286

/*
 * @lc app=leetcode id=3286 lang=kotlin
 *
 * [3286] Find a Safe Walk Through a Grid
 */
import java.util.PriorityQueue
import kotlin.math.abs

// @lc code=start
class Solution {
    data class Status(val x: Int, val y: Int, val health: Int)
    fun findSafeWalk(grid: List<List<Int>>, health: Int): Boolean {
        val targetY = grid.size - 1
        val targetX = grid.first().size - 1
        val que = PriorityQueue<Status>(
            compareBy<Status> { -it.health }
            .thenBy { abs(it.y - targetY).plus(abs(it.x - targetX)) }
        )
        que.add(Status(0, 0, health))
        val hashVisited = Array(grid.size) { BooleanArray(grid.first().size) }

        while (que.isNotEmpty()) {
            val status = que.poll()
            if (hashVisited[status.y][status.x]) continue
            hashVisited[status.y][status.x] = true
            println(status)
            val currentHealth = status.health - grid[status.y][status.x]
            if (currentHealth <= 0) continue
            if (status.x == targetX && status.y == targetY) return true
            for ((dx, dy) in listOf(1 to 0, 0 to 1, -1 to 0, 0 to -1)) {
                val nextX = status.x + dx
                val nextY = status.y + dy
                if (nextX in grid.first().indices && nextY in grid.indices) {
                    que.add(Status(nextX, nextY, currentHealth))
                }
            }
        }
        return false
    }
}
// @lc code=end

