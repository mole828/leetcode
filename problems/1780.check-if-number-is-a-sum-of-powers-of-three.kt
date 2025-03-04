/*
 * @lc app=leetcode id=1780 lang=kotlin
 *
 * [1780] Check if Number is a Sum of Powers of Three
 */

// @lc code=start
class Solution {
    fun checkPowersOfThree(n: Int): Boolean {
        val threeNums = listOf(
            1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683,
            59049, 177147, 531441, 1594323, 4782969, 14348907,
            43046721, 129140163, 387420489, 1162261467
        )
        var num = n
        for (i in (threeNums.size-1).downTo(0)) {
            if (num >= threeNums[i]) {
                num -= threeNums[i]
            }
        }
        return num == 0
    }

    fun myGuess() {
        var total = 0.0
        var i = 0.0
        while (total < 1000000000) {
            val newNum = Math.pow(3.0, i)
            require(newNum > total) {
                "newNum: $newNum, total: $total"
            }
            total += newNum
            i += 1
        }
    }
}
// @lc code=end

fun main() {
    Solution().myGuess()
    println(Solution().checkPowersOfThree(12)) // true
    println(Solution().checkPowersOfThree(91)) // true
    println(Solution().checkPowersOfThree(21)) // false
}
