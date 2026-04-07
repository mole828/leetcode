package problems.p2069
/*
 * @lc app=leetcode id=2069 lang=kotlin
 *
 * [2069] Walking Robot Simulation II
 */

// @lc code=start
data class Complix(val x: Int, val y: Int) {
    operator fun plus(other: Complix): Complix {
        return Complix(x + other.x, y + other.y)
    }

    operator fun times(other: Complix): Complix {
        return Complix(
            x * other.x - y * other.y,
            x * other.y + y * other.x
        )
    }
}

class Robot(val width: Int, val height: Int) {
    private var place = Complix(0, 0)
    private var direction = Complix(1, 0) // East
    private val turnLeft = Complix(0, 1)
    private val perimeter = 2 * (width + height) - 4

    fun step(num: Int) {
        if (num == 0) return

        var remain = num % perimeter
        // 走完整圈时，题目要求停在 (0,0) 且方向为 South
        if (remain == 0) remain = perimeter

        repeat(remain) {
            var next = place + direction
            if (next.x !in 0..<width || next.y !in 0..<height) {
                direction *= turnLeft
                next = place + direction
            }
            place = next
        }
    }

    fun getPos(): IntArray {
        return intArrayOf(place.x, place.y)
    }

    fun getDir(): String {
        return when (direction) {
            Complix(1, 0) -> "East"
            Complix(0, 1) -> "North"
            Complix(-1, 0) -> "West"
            Complix(0, -1) -> "South"
            else -> throw IllegalStateException("Invalid direction")
        }
    }
}

/**
 * Your Robot object will be instantiated and called as such:
 * var obj = Robot(width, height)
 * obj.step(num)
 * var param_2 = obj.getPos()
 * var param_3 = obj.getDir()
 */
// @lc code=end
