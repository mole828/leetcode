package problems.p2463
/*
 * @lc app=leetcode id=2463 lang=kotlin
 *
 * [2463] Minimum Total Distance Traveled
 */

// @lc code=start
const val INF = 1_000_000_000_000_000L
class Solution {
    fun minimumTotalDistance(robot: List<Int>, factory: Array<IntArray>): Long {
        val robot = robot.sorted()
        val factory = factory.sortedBy { it[0] }
        val cache = mutableMapOf<Pair<Int, Int>, Long>()
        fun dfs(robotIndex: Int, factoryIndex: Int): Long = cache.getOrPut(Pair(robotIndex, factoryIndex)) {
            if (robotIndex == robot.size) return 0L
            if (factoryIndex == factory.size) return INF
            val (factoryPos, capacity) = factory[factoryIndex]
            var minDistance = dfs(robotIndex, factoryIndex + 1)
            var distance = 0L
            for (i in 0 until capacity) {
                if (robotIndex + i >= robot.size) break
                distance += kotlin.math.abs(robot[robotIndex + i] - factoryPos)
                minDistance = minOf(minDistance, distance + dfs(robotIndex + i + 1, factoryIndex + 1))
            }
            minDistance
        }
        return dfs(0, 0)
    }
}
// @lc code=end

