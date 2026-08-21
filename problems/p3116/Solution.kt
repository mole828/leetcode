package p3116
/*
 * @lc app=leetcode id=3116 lang=kotlin
 *
 * [3116] Kth Smallest Amount With Single Denomination Combination
 */
// @lc code=start
class Solution {
    private fun gcd(a: Long, b: Long): Long {
        var x = a
        var y = b
        while (y != 0L) {
            val remainder = x % y
            x = y
            y = remainder
        }
        return x
    }

    fun findKthSmallest(coins: IntArray, k: Int): Long {
        val target = k.toLong()

        fun check(x: Long): Boolean {
            var count = 0L

            for (mask in 1 until (1 shl coins.size)) {
                var lcmResult = 1L

                for (j in coins.indices) {
                    if ((mask and (1 shl j)) != 0) {
                        val coin = coins[j].toLong()
                        val factor = coin / gcd(lcmResult, coin)

                        // Once the LCM is greater than x, this subset contributes 0.
                        if (lcmResult > x / factor) {
                            lcmResult = x + 1
                            break
                        }
                        lcmResult *= factor
                    }
                }

                if (lcmResult <= x) {
                    val contribution = x / lcmResult
                    if (Integer.bitCount(mask) % 2 == 1) {
                        count += contribution
                    } else {
                        count -= contribution
                    }
                }
            }

            return count >= target
        }

        var left = 1L
        var right = coins.min().toLong() * target

        while (left < right) {
            val middle = left + (right - left) / 2
            if (check(middle)) {
                right = middle
            } else {
                left = middle + 1
            }
        }

        return left
    }
}
// @lc code=end
