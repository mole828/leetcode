package p3312

/*
 * @lc app=leetcode id=3312 lang=kotlin
 *
 * [3312] Sorted GCD Pair Queries
 */

// @lc code=start
class Solution {
    fun gcdValues(nums: IntArray, queries: LongArray): IntArray {
        val max = nums.maxOrNull()!!
        val frequency = IntArray(max + 1)
        for (num in nums) frequency[num]++

        // exactPairs[d] is the number of pairs whose gcd is exactly d.
        val exactPairs = LongArray(max + 1)
        for (d in max downTo 1) {
            var divisibleCount = 0L
            var multiple = d
            while (multiple <= max) {
                divisibleCount += frequency[multiple]
                multiple += d
            }

            var pairs = divisibleCount * (divisibleCount - 1) / 2
            multiple = d + d
            while (multiple <= max) {
                pairs -= exactPairs[multiple]
                multiple += d
            }
            exactPairs[d] = pairs
        }

        // prefixPairs[d] is the number of pairs with gcd <= d.
        val prefixPairs = LongArray(max + 1)
        for (d in 1..max) {
            prefixPairs[d] = prefixPairs[d - 1] + exactPairs[d]
        }

        return IntArray(queries.size) { index ->
            // queries are zero-based positions in the sorted gcd list.
            val target = queries[index]
            var left = 1
            var right = max
            while (left < right) {
                val middle = left + (right - left) / 2
                if (prefixPairs[middle] > target) right = middle
                else left = middle + 1
            }
            left
        }
    }
}
// @lc code=end
