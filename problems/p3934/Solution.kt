package p3934

/*
 * @lc app=leetcode id=3934 lang=kotlin
 *
 * [3934] Smallest Unique Subarray
 *
 * https://leetcode.com/problems/smallest-unique-subarray/description/
 *
 * algorithms
 * Hard (39.91%)
 * Likes:    128
 * Dislikes: 8
 * Total Accepted:    21.2K
 * Total Submissions: 39.4K
 * Testcase Example:  '[3,3,3]'
 *
 * You are given an integer array nums.
 * 
 * Find the minimum length of a subarray that is not identical to any other
 * subarray in nums.
 * 
 * Return an integer denoting the minimum possible length of such a subarray.
 * 
 * Two subarrays are considered identical if they have the same length and the
 * same elements in corresponding positions.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [3,3,3]
 * 
 * Output: 3
 * 
 * Explanation:
 * 
 * 
 * Subarrays of length 1: [3] → appears 3 times
 * Subarrays of length 2: [3, 3] → appears 2 times
 * Subarrays of length 3: [3, 3, 3] → appears once
 * 
 * 
 * The subarray [3, 3, 3] is unique, so the smallest unique subarray length is
 * 3.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [2,1,2,3,3]
 * 
 * Output: 1
 * 
 * Explanation:
 * 
 * Subarrays of length 1:
 * 
 * 
 * [2] → appears 2 times
 * [1] → appears once
 * [3] → appears 2 times
 * 
 * The subarray [1] is unique, so the smallest unique subarray length is 1.
 * 
 * Example 3:
 * 
 * 
 * Input: nums = [1,1,2,2,1]
 * 
 * Output: 2
 * 
 * Explanation:
 * 
 * Subarrays of length 1:
 * 
 * 
 * [1] → appears 3 times
 * [2] → appears 2 times
 * 
 * 
 * Subarrays of length 2:
 * 
 * 
 * [1, 1] → appears once
 * [1, 2] → appears once
 * [2, 2] → appears once
 * [2, 1] → appears once
 * 
 * There is at least one subarray of length 2 that is unique, so the smallest
 * unique subarray length is 2.
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= nums.length <= 10^5
 * 1 <= nums[i] <= 10^5
 * 
 * 
 */

// @lc code=start
class Solution {
    fun smallestUniqueSubarray(nums: IntArray): Int {
        val n = nums.size
        if (n == 1) return 1

        val base1 = 1315423911L
        val mod1 = 1_000_000_007L
        val base2 = 2654435761L
        val mod2 = 1_000_000_009L

        val pow1 = LongArray(n + 1)
        val pow2 = LongArray(n + 1)
        pow1[0] = 1L
        pow2[0] = 1L
        for (i in 1..n) {
            pow1[i] = (pow1[i - 1] * base1) % mod1
            pow2[i] = (pow2[i - 1] * base2) % mod2
        }

        fun hasUniqueOfLength(len: Int): Boolean {
            var h1 = 0L
            var h2 = 0L
            for (i in 0 until len) {
                val v = nums[i].toLong()
                h1 = (h1 * base1 + v) % mod1
                h2 = (h2 * base2 + v) % mod2
            }

            fun pack(a: Long, b: Long): Long = (a shl 32) or (b and 0xFFFF_FFFFL)

            val counts = HashMap<Long, Int>(n * 2)
            var key = pack(h1, h2)
            counts[key] = 1

            val p1 = pow1[len - 1]
            val p2 = pow2[len - 1]

            for (i in 1..(n - len)) {
                val outVal = nums[i - 1].toLong()
                val inVal = nums[i + len - 1].toLong()

                h1 = ((h1 - (outVal * p1) % mod1 + mod1) % mod1 * base1 + inVal) % mod1
                h2 = ((h2 - (outVal * p2) % mod2 + mod2) % mod2 * base2 + inVal) % mod2

                key = pack(h1, h2)
                counts[key] = (counts[key] ?: 0) + 1
            }

            for (count in counts.values) {
                if (count == 1) return true
            }
            return false
        }

        var left = 1
        var right = n
        var ans = n

        while (left <= right) {
            val mid = left + (right - left) / 2
            if (hasUniqueOfLength(mid)) {
                ans = mid
                right = mid - 1
            } else {
                left = mid + 1
            }
        }

        return ans
    }
}
// @lc code=end

