package p3751

/*
 * @lc app=leetcode id=3751 lang=kotlin
 *
 * [3751] Total Waviness of Numbers in Range I
 */

// @lc code=start
class Solution {
    fun totalWaviness(num1: Int, num2: Int): Int {
        fun countWavy(num: Int): Int {
            val s = num.toString()
            var count = 0
            for (i in 1 until s.length - 1) {
                if (s[i] > s[i - 1] && s[i] > s[i + 1] || s[i] < s[i - 1] && s[i] < s[i + 1]) {
                    count++
                }
            }
            return count
        }
        var total = 0
        for (i in num1..num2) {
            total += countWavy(i)
        }
        return total
    }
}
// @lc code=end

