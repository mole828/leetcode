import kotlin.math.sqrt

/*
 * @lc app=leetcode id=3296 lang=kotlin
 *
 * [3296] Minimum Number of Seconds to Make Mountain Height Zero
 */

// @lc code=start
class _Solution {
    fun minNumberOfSeconds(mountainHeight: Int, workerTimes: IntArray): Long {
        fun workerInTime(workerTime: Int, time: Long): Int {
            var floor = 0
            var usedTime = 0L
            while (usedTime < time) {
                floor += 1
                usedTime += workerTime * floor
            }
            return floor - 1
        }
        var right = (1..mountainHeight).sumOf {
            workerTimes[0].toLong() * it
        }
        var left = workerTimes.min().toLong()
        while (left <= right) {
            val mid = (left + right) / 2
            val sumOfFloor = workerTimes.sumOf { workerInTime(it, mid) }
            if (sumOfFloor >= mountainHeight) {
                right = mid - 1
            } else {
                left = mid + 1
            }
            println("$left, $right, $sumOfFloor")
        }
        return right
    }
}

class Solution {
    fun minNumberOfSeconds(mountainHeight: Int, workerTimes: IntArray): Long {
        // 计算某个工人在 time 时间内能降低的高度
        fun getMaxHeight(workerTime: Int, timeLimit: Long): Long {
            // 根据等差数列求和公式: workerTime * n * (n + 1) / 2 <= timeLimit
            // 转换为: n^2 + n - (2 * timeLimit / workerTime) <= 0
            val target = 2.0 * timeLimit / workerTime
            return ((-1.0 + sqrt(1.0 + 4.0 * target)) / 2.0).toLong()
        }

        var left = 0L
        // 初始右边界：取最快的工人独立完成所有高度的时间
        // 如果高度为 H，最快工时为 W，则时间为 W * H * (H + 1) / 2
        val minW = workerTimes.min().toLong()
        var right = minW * mountainHeight * (mountainHeight + 1L) / 2

        var ans = right

        while (left <= right) {
            val mid = left + (right - left) / 2
            var totalHeight = 0L

            for (w in workerTimes) {
                totalHeight += getMaxHeight(w, mid)
                // 提前剪枝，防止 Long 溢出或无效计算
                if (totalHeight >= mountainHeight) break
            }

            if (totalHeight >= mountainHeight) {
                ans = mid // 记录当前可行解
                right = mid - 1
            } else {
                left = mid + 1
            }
        }
        return ans
    }
}
// @lc code=end

//println(Solution().minNumberOfSeconds(4, intArrayOf(1, 3, 1)))
println(Solution().minNumberOfSeconds(100000, intArrayOf(1)))