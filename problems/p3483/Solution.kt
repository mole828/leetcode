package p3483

/*
 * @lc app=leetcode id=3483 lang=kotlin
 *
 * [3483] Unique 3-Digit Even Numbers
 */

// @lc code=start
class Solution {
    fun totalNumbers(digits: IntArray): Int {
        val numbers = mutableSetOf<Int>()
        for (i in digits.indices) {
            if (digits[i] == 0) continue
            for (j in digits.indices) {
                if (j == i) continue
                for (k in digits.indices) {
                    if (k == i || k == j || digits[k] % 2 != 0) continue
                    numbers.add(digits[i] * 100 + digits[j] * 10 + digits[k])
                }
            }
        }
        return numbers.size
    }
}
// @lc code=end
