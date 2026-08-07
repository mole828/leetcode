/*
 * @lc app=leetcode id=3348 lang=kotlin
 *
 * [3348] Smallest Divisible Digit Product II
 *
 * https://leetcode.com/problems/smallest-divisible-digit-product-ii/description/
 *
 * algorithms
 * Hard (14.90%)
 * Likes:    77
 * Dislikes: 25
 * Total Accepted:    7.9K
 * Total Submissions: 39K
 * Testcase Example:  '"1234"\n256'
 *
 * You are given a string num which represents a positive integer, and an
 * integer t.
 * 
 * A number is called zero-free if none of its digits are 0.
 * 
 * Return a string representing the smallest zero-free number greater than or
 * equal to num such that the product of its digits is divisible by t. If no
 * such number exists, return "-1".
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: num = "1234", t = 256
 * 
 * Output: "1488"
 * 
 * Explanation:
 * 
 * The smallest zero-free number that is greater than 1234 and has the product
 * of its digits divisible by 256 is 1488, with the product of its digits equal
 * to 256.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: num = "12355", t = 50
 * 
 * Output: "12355"
 * 
 * Explanation:
 * 
 * 12355 is already zero-free and has the product of its digits divisible by
 * 50, with the product of its digits equal to 150.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: num = "11111", t = 26
 * 
 * Output: "-1"
 * 
 * Explanation:
 * 
 * No number greater than 11111 has the product of its digits divisible by
 * 26.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 2 <= num.length <= 2 * 10^5
 * num consists only of digits in the range ['0', '9'].
 * num does not contain leading zeros.
 * 1 <= t <= 10^14
 * 
 * 
 */
package p3348

// TODO: 没完全理解
// @lc code=start
class Solution {
    fun smallestNumber(num: String, t: Long): String {
        // A digit product can only contain the prime factors 2, 3, 5 and 7.
        var rest = t
        var need2 = 0
        var need3 = 0
        var need5 = 0
        var need7 = 0

        while (rest % 2L == 0L) {
            rest /= 2L
            need2++
        }
        while (rest % 3L == 0L) {
            rest /= 3L
            need3++
        }
        while (rest % 5L == 0L) {
            rest /= 5L
            need5++
        }
        while (rest % 7L == 0L) {
            rest /= 7L
            need7++
        }
        if (rest != 1L) return "-1"

        val factor2 = intArrayOf(0, 0, 1, 0, 2, 0, 1, 0, 3, 0)
        val factor3 = intArrayOf(0, 0, 0, 1, 0, 0, 1, 0, 0, 2)
        val factor5 = intArrayOf(0, 0, 0, 0, 0, 1, 0, 0, 0, 0)
        val factor7 = intArrayOf(0, 0, 0, 0, 0, 0, 0, 1, 0, 0)

        val stride5 = need7 + 1
        val stride3 = (need5 + 1) * (need7 + 1)
        val stride2 = (need3 + 1) * stride3
        val stateCount = (need2 + 1) * stride2

        fun stateIndex(two: Int, three: Int, five: Int, seven: Int): Int {
            return two * stride2 + three * stride3 + five * stride5 + seven
        }

        // minDigits[state] is the minimum number of digits needed to cover
        // the prime exponents represented by state. Exponents are capped at
        // the exponents required by t, so the state space is small (under
        // 504,000 states for the given limits).
        val inf = 1_000_000
        val minDigits = IntArray(stateCount) { inf }
        minDigits[0] = 0
        for (two in 0..need2) {
            for (three in 0..need3) {
                for (five in 0..need5) {
                    for (seven in 0..need7) {
                        if (two == 0 && three == 0 && five == 0 && seven == 0) continue

                        val current = stateIndex(two, three, five, seven)
                        var best = inf
                        for (digit in 2..9) {
                            val previous = stateIndex(
                                maxOf(0, two - factor2[digit]),
                                maxOf(0, three - factor3[digit]),
                                maxOf(0, five - factor5[digit]),
                                maxOf(0, seven - factor7[digit]),
                            )
                            best = minOf(best, minDigits[previous] + 1)
                        }
                        minDigits[current] = best
                    }
                }
            }
        }

        // Fill a suffix with the lexicographically smallest possible digits.
        fun fillSmallest(
            result: StringBuilder,
            length: Int,
            initialTwo: Int,
            initialThree: Int,
            initialFive: Int,
            initialSeven: Int,
        ): Boolean {
            var two = initialTwo
            var three = initialThree
            var five = initialFive
            var seven = initialSeven

            var position = 0
            while (position < length) {
                val left = length - position - 1
                var chosen = 0
                for (digit in 1..9) {
                    val nextTwo = maxOf(0, two - factor2[digit])
                    val nextThree = maxOf(0, three - factor3[digit])
                    val nextFive = maxOf(0, five - factor5[digit])
                    val nextSeven = maxOf(0, seven - factor7[digit])
                    if (minDigits[stateIndex(nextTwo, nextThree, nextFive, nextSeven)] <= left) {
                        chosen = digit
                        two = nextTwo
                        three = nextThree
                        five = nextFive
                        seven = nextSeven
                        break
                    }
                }
                if (chosen == 0) return false
                result.append(('0'.code + chosen).toChar())
                position++
            }
            return true
        }

        val n = num.length
        val prefixTwo = IntArray(n + 1)
        val prefixThree = IntArray(n + 1)
        val prefixFive = IntArray(n + 1)
        val prefixSeven = IntArray(n + 1)
        prefixTwo[0] = need2
        prefixThree[0] = need3
        prefixFive[0] = need5
        prefixSeven[0] = need7

        // prefix arrays are only valid before the first zero. A zero cannot
        // occur in the unchanged prefix of a zero-free answer.
        var firstZero = n
        for (i in 0 until n) {
            val digit = num[i] - '0'
            if (digit == 0) {
                firstZero = i
                break
            }
            prefixTwo[i + 1] = maxOf(0, prefixTwo[i] - factor2[digit])
            prefixThree[i + 1] = maxOf(0, prefixThree[i] - factor3[digit])
            prefixFive[i + 1] = maxOf(0, prefixFive[i] - factor5[digit])
            prefixSeven[i + 1] = maxOf(0, prefixSeven[i] - factor7[digit])
        }

        if (firstZero == n && prefixTwo[n] == 0 && prefixThree[n] == 0 &&
            prefixFive[n] == 0 && prefixSeven[n] == 0
        ) {
            return num
        }

        // The rightmost possible changed position gives the smallest number.
        val lastPivot = minOf(n - 1, firstZero)
        for (pivot in lastPivot downTo 0) {
            val originalDigit = num[pivot] - '0'
            val suffixLength = n - pivot - 1

            for (digit in (originalDigit + 1) until 10) {
                val nextTwo = maxOf(0, prefixTwo[pivot] - factor2[digit])
                val nextThree = maxOf(0, prefixThree[pivot] - factor3[digit])
                val nextFive = maxOf(0, prefixFive[pivot] - factor5[digit])
                val nextSeven = maxOf(0, prefixSeven[pivot] - factor7[digit])
                if (minDigits[stateIndex(nextTwo, nextThree, nextFive, nextSeven)] > suffixLength) {
                    continue
                }

                val answer = StringBuilder(n)
                answer.append(num, 0, pivot)
                answer.append(('0'.code + digit).toChar())
                fillSmallest(answer, suffixLength, nextTwo, nextThree, nextFive, nextSeven)
                return answer.toString()
            }
        }

        // Any number with more digits is already greater than num. Usually
        // n + 1 is enough, but a large t can require a few more digits.
        val minimumLength = minDigits[stateIndex(need2, need3, need5, need7)]
        val length = maxOf(n + 1, minimumLength)
        val answer = StringBuilder(length)
        if (fillSmallest(answer, length, need2, need3, need5, need7)) {
            return answer.toString()
        }
        return "-1"


    }
}
// @lc code=end
