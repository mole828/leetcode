package p3753

/*
 * @lc app=leetcode id=3753 lang=kotlin
 *
 * [3753] Total Waviness of Numbers in Range II
 */

// @lc code=start
class Solution {
    @Deprecated("Time limit exceeded")
    fun totalWaviness1(num1: Long, num2: Long): Long {
        fun countWavy(num: Long): Long {
            val s = num.toString()
            var count = 0L
            for (i in 1 until s.length - 1) {
                if (s[i] > s[i - 1] && s[i] > s[i + 1] || s[i] < s[i - 1] && s[i] < s[i + 1]) {
                    count++
                }
            }
            return count
        }
        var total = 0L
        for (i in num1..num2) {
            total += countWavy(i)
        }
        return total
    }
    
    fun totalWaviness(num1: Long, num2: Long): Long {
        val low = num1.toString().map { it - '0' }
        val high = num2.toString().map { it - '0' }
        val offset = high.size - low.size
        data class State(
            val i: Int,
            val lastCmp: Int,
            val lastDigit: Int,
            val lowLimit: Boolean,
            val highLimit: Boolean
        )
        val memo = HashMap<State, Pair<Long, Long>>()

        fun dfs(state: State): Pair<Long, Long> {
            if (state.i == high.size) return 0L to 1L

            return memo.getOrPut(state) {
                val (i, lastCmp, lastDigit, lowLimit, highLimit) = state

                val lo = if (lowLimit && i >= offset) low[i - offset] else 0
                val hi = if (highLimit) high[i] else 9
                val hasDigit = !lowLimit || i > offset
                var total = 0L
                var count = 0L

                for (digit in lo..hi) {
                    val cmp = if (hasDigit) digit.compareTo(lastDigit) else 0
                    val next = State(i + 1, cmp, digit, lowLimit && digit == lo, highLimit && digit == hi)
                    val (childTotal, childCount) = dfs(next)
                    total += childTotal + if (cmp * lastCmp < 0) childCount else 0
                    count += childCount
                }

                total to count
            }
        }

        return dfs(State(0, 0, 0, lowLimit = true, highLimit = true)).first
    }
}
// @lc code=end
