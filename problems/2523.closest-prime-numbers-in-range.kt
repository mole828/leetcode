/*
 * @lc app=leetcode id=2523 lang=kotlin
 *
 * [2523] Closest Prime Numbers in Range
 */
package p2523


// @lc code=start
class Solution {
    fun closestPrimes(left: Int, right: Int): IntArray {
        val primesBoolean = BooleanArray(right + 1) { true }
        primesBoolean[0] = false
        primesBoolean[1] = false
        for (i in 2..right) {
            if (primesBoolean[i]) {
                for (j in 2 * i..right step i) {
                    primesBoolean[j] = false
                }
            }
        }

        var minDiff = Int.MAX_VALUE
        var minPair = intArrayOf(-1, -1)

        var lastPrime: Int = -1
        for (i in left..right) {
            if (primesBoolean[i]) {
                lastPrime = i
                break
            }
        }
        if (lastPrime == -1) {
            return intArrayOf(-1, -1)
        }

        for (i in (lastPrime+1)..right) {
            if (primesBoolean[i]) {
                val diff = i - lastPrime
                if (diff < minDiff) {
                    minDiff = diff
                    minPair = intArrayOf(lastPrime, i)
                }
                lastPrime = i
            }
        }
        
        return minPair
    }
}
// @lc code=end

fun main() {
    println(Solution().closestPrimes(10, 20).toList()) // [11, 13]
}