package p3336
/*
 * @lc app=leetcode id=3336 lang=kotlin
 *
 * [3336] Find the Number of Subsequences With Equal GCD
 */
// @lc code=start
class Solution {
    fun subsequencePairCount(nums: IntArray): Int {
        val maxGcd = nums.max()
        var dp = Array(maxGcd + 1) { IntArray(maxGcd + 1) }
        dp[0][0] = 1

        for (num in nums) {
            val next = Array(maxGcd + 1) { IntArray(maxGcd + 1) }

            for (firstGcd in 0..maxGcd) {
                for (secondGcd in 0..maxGcd) {
                    val count = dp[firstGcd][secondGcd]
                    if (count == 0) continue

                    next[firstGcd].add(secondGcd, count)
                    next[gcd(firstGcd, num)].add(secondGcd, count)
                    next[firstGcd].add(gcd(secondGcd, num), count)
                }
            }

            dp = next
        }

        return (1..maxGcd).fold(0) { answer, gcd ->
            (answer + dp[gcd][gcd]) % MOD
        }
    }

    private fun gcd(a: Int, b: Int): Int =
        if (a == 0) b else gcd(b % a, a)

    private fun IntArray.add(index: Int, value: Int) {
        this[index] = (this[index] + value) % MOD
    }

    private companion object {
        const val MOD = 1_000_000_007
    }
}
// @lc code=end
