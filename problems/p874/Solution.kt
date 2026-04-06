package problems.p874
/*
 * @lc app=leetcode id=874 lang=kotlin
 *
 * [874] Walking Robot Simulation
 */
// @lc code=start
data class Complix(val x: Int, val y: Int) {
    operator fun times(other: Complix): Complix {
        return Complix(x * other.x - y * other.y, x * other.y + y * other.x)
    }
    operator fun plus(other: Complix): Complix {
        return Complix(x + other.x, y + other.y)
    }
}
class Solution {
    fun robotSim(commands: IntArray, obstacles: Array<IntArray>): Int {
        val obstaclesSet = obstacles.map { Complix(it[0], it[1]) }.toSet()
        // println(obstaclesSet)
        var place = Complix(0, 0)
        var direction = Complix(0, 1)
        var max = 0
        for (command in commands) {
            when (command) {
                -2 -> direction *= Complix(0, 1)
                -1 -> direction *= Complix(0, -1)
                else -> {
                    repeat(command) {
                        val next = place + direction
                        if (next !in obstaclesSet) {
                            place = next
                            // println(place)
                            max = maxOf(max, place.x * place.x + place.y * place.y)
                        }
                    }
                }
            }
        }
        return max
    }
}
// @lc code=end

