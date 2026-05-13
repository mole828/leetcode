package p3660

import p2463.INF

/*
 * @lc app=leetcode id=3660 lang=kotlin
 *
 * [3660] Jump Game IX
 */

// @lc code=start
class Solution {
    @Deprecated("TLE")
    fun maxValue0(nums: IntArray): IntArray {
        fun jumpAble(i: Int, j: Int): Boolean {
            if (i == j) return false
            if( nums[j] < nums[i] && j > i) return true
            if( nums[j] > nums[i] && j < i) return true
            return false
        }
        return nums.mapIndexed { i, num ->
            var max = 0
            val hasMeet = BooleanArray(nums.size)
            val queue = ArrayDeque<Int>()
            queue.add(i)
            while (queue.isNotEmpty()) {
                val idx = queue.removeFirst()
                if (hasMeet[idx]) continue
                hasMeet[idx] = true
                max = maxOf(max, nums[idx])
                for (j in nums.indices) {
                    if (jumpAble(idx, j) && !hasMeet[j]) {
                        queue.add(j)
                    }
                }
            }
            max
        }.toIntArray()
    }

    fun maxValue(nums: IntArray): IntArray {
        val n = nums.size
        val preMax = IntArray(n)
        preMax[0] = nums[0]
        for (i in 1 until n) {
            preMax[i] = maxOf(preMax[i - 1], nums[i])
        }

        val ans = IntArray(n)
        var sufMin = Int.MAX_VALUE
        for (i in n - 1 downTo 0) {
            ans[i] = if (preMax[i] <= sufMin) {
                preMax[i]
            } else {
                if (i == n - 1) preMax[i] else ans[i + 1]
            }
            sufMin = minOf(sufMin, nums[i])
        }
        return ans
    }
}
// @lc code=end

